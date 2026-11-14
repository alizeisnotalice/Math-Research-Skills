#!/usr/bin/env python3
"""Run a saved math script in an existing Python environment, with bounded lifetime."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time
import uuid


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def check_data_mount(path):
    if (str(path) == '/Volumes/data' or str(path).startswith('/Volumes/data/')) and not Path('/Volumes/data').is_mount():
        raise ValueError('data is not mounted; refusing to fall back to the system disk')


def environment_candidates(explicit, workdir):
    if explicit:
        return [explicit]
    candidates = [str(workdir / '.venv/bin/python')]
    if os.environ.get('VIRTUAL_ENV'):
        candidates.append(str(Path(os.environ['VIRTUAL_ENV']) / 'bin/python'))
    candidates += [sys.executable, str(Path.home() / '.venvs/main/bin/python'),
                   str(Path.home() / '.venv/bin/python')]
    return list(dict.fromkeys(candidates))


def select_environment(candidates, modules):
    attempts = []
    code = '''import importlib, json, sys
modules = [importlib.import_module(name) for name in json.loads(sys.argv[1])]
print(json.dumps({'executable':sys.executable,'version':sys.version.split()[0],
'modules':{name:getattr(module,'__version__','imported') for name,module in zip(json.loads(sys.argv[1]),modules)}}))'''
    for candidate in candidates:
        executable = shutil.which(os.path.expanduser(candidate))
        if not executable or not Path(executable).is_file():
            attempts.append({'candidate':candidate,'error':'not executable'})
            continue
        env = os.environ.copy()
        env['PYTHONDONTWRITEBYTECODE'] = '1'
        try:
            result = subprocess.run([executable, '-c', code, json.dumps(modules)],
                                    capture_output=True, text=True, timeout=20, env=env)
            if result.returncode == 0:
                return executable, json.loads(result.stdout), attempts
            attempts.append({'candidate':candidate,'error':result.stderr[-2000:]})
        except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
            attempts.append({'candidate':candidate,'error':str(exc)})
    raise ValueError('No existing environment can import the required modules: ' + json.dumps(attempts, ensure_ascii=False))


def stop_group(process):
    if process.poll() is not None:
        return
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    try:
        process.wait(timeout=3)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--python', dest='interpreter')
    parser.add_argument('--require', action='append', default=[], metavar='MODULE')
    parser.add_argument('--workdir', type=Path)
    parser.add_argument('--log-root', type=Path)
    parser.add_argument('--timeout', type=float, default=300)
    parser.add_argument('script', type=Path)
    parser.add_argument('script_args', nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    try:
        script = args.script.expanduser().resolve(strict=True)
        if not script.is_file() or script.suffix != '.py':
            raise ValueError('script must be an existing .py file')
        workdir = (args.workdir or script.parent).expanduser().resolve(strict=True)
        if not workdir.is_dir():
            raise ValueError('workdir must be an existing directory')
        if not 0 < args.timeout < float('inf'):
            raise ValueError('timeout must be finite and positive')
        modules = list(dict.fromkeys(args.require))
        if any(not re.fullmatch(r'[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*', name) for name in modules):
            raise ValueError('--require expects importable module names')
        check_data_mount(workdir)
        explicit = args.interpreter or os.environ.get('MATH_RESEARCH_PYTHON')
        executable, runtime, attempts = select_environment(environment_candidates(explicit, workdir), modules)
        default_root = next((os.environ[key] for key in ('MATH_RESEARCH_RUN_DIR','TMPDIR','TMP','TEMP','XDG_CACHE_HOME') if os.environ.get(key)),
                            '/Volumes/data/CodexTemp/Math-Research-Skills')
        log_root = (args.log_root or Path(default_root) / 'python-math-runs').expanduser().absolute()
        check_data_mount(log_root)
        log_root.mkdir(parents=True, exist_ok=True)
        log_root = log_root.resolve()
        check_data_mount(log_root)
        run_dir = log_root / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8])
        run_dir.mkdir()
        snapshot = script.read_bytes()
        (run_dir/'input-script.py').write_bytes(snapshot)
    except (OSError, ValueError) as exc:
        print(json.dumps({'state':'input-or-environment-error','error':str(exc)},ensure_ascii=False), file=sys.stderr)
        return 2

    command = [executable, str(script), *args.script_args]
    report = {'state':'running','started_at':utc_now(),'script':str(script),
              'script_sha256':hashlib.sha256(snapshot).hexdigest(),'command':command,
              'workdir':str(workdir),'runtime':runtime,'environment_attempts':attempts,
              'timeout_seconds':args.timeout,'log_dir':str(run_dir),
              'stdout':str(run_dir/'stdout.txt'),'stderr':str(run_dir/'stderr.txt')}
    status_path = run_dir/'run.json'
    def save():
        status_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    save()
    print(json.dumps({'log_dir':str(run_dir),'runtime':runtime},ensure_ascii=False),flush=True)
    env = os.environ.copy()
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    started = time.monotonic()
    process = None
    old_handlers = {}
    def cancel(signum, frame):
        raise KeyboardInterrupt
    try:
        old_handlers = {sig:signal.signal(sig,cancel) for sig in (signal.SIGINT,signal.SIGTERM)}
        with (run_dir/'stdout.txt').open('w') as stdout, (run_dir/'stderr.txt').open('w') as stderr:
            process = subprocess.Popen(command, cwd=workdir, env=env, stdout=stdout,
                                       stderr=stderr, start_new_session=True)
            report['pid'] = process.pid
            save()
            try:
                code = process.wait(timeout=args.timeout)
                report['state'] = 'succeeded' if code == 0 else 'failed'
                exit_code = code if code >= 0 else 128-code
            except subprocess.TimeoutExpired:
                stop_group(process)
                report['state'] = 'timed-out'
                exit_code = 124
    except KeyboardInterrupt:
        if process is not None:
            stop_group(process)
        report['state'] = 'cancelled'
        exit_code = 130
    except OSError as exc:
        report.update(state='launch-error',error=str(exc))
        exit_code = 2
    finally:
        if process is not None:
            stop_group(process)
        for sig, handler in old_handlers.items():
            signal.signal(sig,handler)
    report.update(exit_code=exit_code,finished_at=utc_now(),elapsed_seconds=round(time.monotonic()-started,3))
    if process is not None:
        report['child_returncode'] = process.returncode
    save()
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
