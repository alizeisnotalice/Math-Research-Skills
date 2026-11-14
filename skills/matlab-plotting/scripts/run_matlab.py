#!/usr/bin/env python3
"""Run one MATLAB .m script; keep an isolated log and machine-readable status."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
import uuid


def find_matlab(explicit=None):
    selected = explicit or os.environ.get('MATLAB_EXECUTABLE')
    if selected:
        candidates = [Path(selected).expanduser()]
    else:
        found = shutil.which('matlab')
        candidates = ([Path(found)] if found else [])
        candidates += sorted(Path('/Applications').glob('MATLAB_R*.app/bin/matlab'), reverse=True)
    for candidate in candidates:
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return candidate.resolve()
    raise FileNotFoundError('MATLAB executable not found. Set --matlab or MATLAB_EXECUTABLE.')


def matlab_string(value):
    return "'" + str(value).replace("'", "''") + "'"


def stop_process(proc):
    # Terminate only the process group created by this invocation, not user sessions.
    if os.name == 'posix':
        try:
            os.killpg(proc.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            pass
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    else:
        proc.kill()
    proc.wait()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('script', nargs='?', type=Path)
    parser.add_argument('--workdir', type=Path, default=Path.cwd())
    parser.add_argument('--matlab', help='Executable path (not MATLAB root)')
    parser.add_argument('--timeout', type=float, default=300, help='Seconds, including startup')
    parser.add_argument('--log-dir', type=Path, help='Parent directory for unique run logs')
    parser.add_argument('--detect', action='store_true', help='Print executable path without starting MATLAB')
    args = parser.parse_args(argv)
    try:
        executable = find_matlab(args.matlab)
        if args.detect:
            print(executable)
            return 0
        if not args.script:
            parser.error('script is required unless --detect is used')
        script = args.script.expanduser().resolve()
        workdir = args.workdir.expanduser().resolve()
        if not script.is_file() or script.suffix.lower() != '.m':
            raise ValueError('script must be an existing .m file')
        if not workdir.is_dir():
            raise ValueError('workdir must be an existing directory')
        if not 0 < args.timeout < float('inf'):
            raise ValueError('timeout must be a finite positive number')
        log_root = (args.log_dir or workdir / 'work' / 'matlab-runs').expanduser().resolve()
        run_dir = log_root / (dt.datetime.now().strftime('%Y%m%d-%H%M%S') + '-' + uuid.uuid4().hex[:8])
        run_dir.mkdir(parents=True)
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    helpers = Path(__file__).resolve().parent
    # The macOS MATLAB shell launcher mishandles apostrophes in -sd.
    # cwd plus MATLAB cd avoids that extra shell-quoting layer.
    statement = f"cd({matlab_string(workdir)}); addpath({matlab_string(helpers)}); run({matlab_string(script)});"
    command = [str(executable), '-batch', statement]
    log_path = run_dir / 'matlab.log'
    status_path = run_dir / 'status.json'
    status = {'state': 'starting', 'script': str(script), 'workdir': str(workdir),
              'command': command, 'log': str(log_path), 'pid': None}

    def save():
        temporary = status_path.with_suffix('.tmp')
        temporary.write_text(json.dumps(status, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        temporary.replace(status_path)

    save()
    print(json.dumps({'status': str(status_path), 'log': str(log_path)}, ensure_ascii=False), flush=True)
    started = time.monotonic()
    code = 1
    proc = None
    terminated_signal = None

    def handle_sigterm(signum, _frame):
        nonlocal terminated_signal
        terminated_signal = signum
        # Do not wait here: signals can interrupt Popen while its wait lock is held.

    previous_sigterm = signal.signal(signal.SIGTERM, handle_sigterm)
    try:
        with log_path.open('w', encoding='utf-8') as log:
            if terminated_signal is not None:
                raise InterruptedError('Cancelled before MATLAB startup')
            proc = subprocess.Popen(command, cwd=workdir, stdout=log, stderr=subprocess.STDOUT,
                                    start_new_session=(os.name == 'posix'))
            # The loop also observes signals received while Popen was returning.
            status.update(state='running', pid=proc.pid)
            save()
            deadline = started + args.timeout
            while True:
                if terminated_signal is not None:
                    stop_process(proc)
                    break
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    stop_process(proc)
                    status.update(state='timed_out', note='Owned process group stopped; partial files may exist.')
                    code = 124
                    break
                try:
                    result = proc.wait(timeout=min(0.2, remaining))
                except subprocess.TimeoutExpired:
                    continue
                code = result if result >= 0 else 128 - result
                status.update(state='succeeded' if result == 0 else 'failed', matlab_returncode=result)
                break
    except KeyboardInterrupt:
        status.update(state='interrupted', note='Owned process group stopped; partial files may exist.')
        code = 130
    except OSError as exc:
        status.update(state='failed', error=str(exc))
        code = 1
    finally:
        # Also clean up when logging/status writes fail after the child starts.
        try:
            if proc is not None and proc.poll() is None:
                stop_process(proc)
        finally:
            signal.signal(signal.SIGTERM, previous_sigterm)
            if terminated_signal is not None:
                code = 128 + terminated_signal
                status.update(state='interrupted', signal='SIGTERM',
                              note='Owned process group stopped; partial files may exist.')
            status.update(exit_code=code, elapsed_seconds=round(time.monotonic() - started, 3))
            save()
    print(json.dumps(status, ensure_ascii=False), flush=True)
    if code:
        print(f'MATLAB did not complete successfully. Inspect {log_path}', file=sys.stderr)
    return code


if __name__ == '__main__':
    sys.exit(main())
