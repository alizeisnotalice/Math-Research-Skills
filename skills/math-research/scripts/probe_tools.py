#!/usr/bin/env python3
"""Discover existing math backends; run small checks only with --smoke."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys


def run(command, timeout, env=None):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True, env=env, start_new_session=True)
    try:
        stdout, stderr = process.communicate(timeout=timeout)
        return {"returncode": process.returncode, "stdout": stdout.strip(),
                "stderr": stderr.strip(), "timed_out": False}
    except subprocess.TimeoutExpired:
        for sig, wait in ((signal.SIGTERM, 3), (signal.SIGKILL, None)):
            try:
                os.killpg(process.pid, sig)
            except ProcessLookupError:
                pass
            try:
                stdout, stderr = process.communicate(timeout=wait)
                break
            except subprocess.TimeoutExpired:
                continue
        return {"returncode": process.returncode, "stdout": stdout.strip(),
                "stderr": stderr.strip(), "timed_out": True}


def discover_applications(applications=Path('/Applications')):
    if not applications.is_dir():
        return [], []
    matlab = sorted(str(p / 'bin/matlab') for p in applications.glob('MATLAB*.app')
                    if (p / 'bin/matlab').is_file())
    kernels = []
    for pattern in ('Wolfram*.app', 'Mathematica*.app'):
        for app in sorted(applications.glob(pattern)):
            for name in ('WolframKernel', 'MathKernel'):
                candidate = app / 'Contents/MacOS' / name
                if candidate.is_file() and os.access(candidate, os.X_OK):
                    kernels.append(str(candidate))
    return matlab, kernels


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--python', default=sys.executable,
                        help='Existing project interpreter; no environment is installed')
    parser.add_argument('--smoke', choices=('python', 'wolfram'), action='append', default=[])
    parser.add_argument('--timeout', type=int, default=30)
    args = parser.parse_args(argv)
    if not 1 <= args.timeout <= 120:
        parser.error('--timeout must be between 1 and 120 seconds')
    python = shutil.which(args.python)
    if not python:
        parser.error('Python interpreter not found: ' + args.python)
    matlab, kernels = discover_applications()
    wolframscript = shutil.which('wolframscript')
    kernel = os.environ.get('WolframKernel') or (kernels[0] if kernels else None)
    python_code = '''import importlib.util, json, sys
names = ['numpy', 'scipy', 'sympy', 'mpmath', 'matplotlib', 'yaml']
print(json.dumps({'executable':sys.executable, 'version':sys.version.split()[0],
'libraries_discovered':{name:importlib.util.find_spec(name) is not None for name in names},
'note':'Discovery alone does not verify imports or numerical execution.'}))'''
    environment = os.environ.copy()
    environment['PYTHONDONTWRITEBYTECODE'] = '1'
    probe = run([python, '-c', python_code], args.timeout, environment)
    report = {'python_probe': probe, 'wolframscript': wolframscript,
              'wolfram_kernel_candidate': kernel, 'matlab_cli_candidates': matlab,
              'matlab_on_path': shutil.which('matlab'), 'smoke': {},
              'note': 'MCP availability must be checked in the current tool inventory.'}
    failed = probe['returncode'] != 0 or probe['timed_out']
    if not failed:
        report['python'] = json.loads(probe['stdout'])
        del report['python_probe']
    for backend in dict.fromkeys(args.smoke):
        if backend == 'python':
            code = '''from fractions import Fraction
import json, importlib.util, sys
value = Fraction(1, 3) + Fraction(1, 6)
assert value == Fraction(1, 2)
result = {'version':sys.version.split()[0], 'rational_sum':str(value)}
if importlib.util.find_spec('sympy') is not None:
    import sympy as sp
    x = sp.Symbol('x')
    residual = sp.simplify(sp.diff(sp.sin(x), x) - sp.cos(x))
    assert residual == 0
    result['sympy_version'] = sp.__version__
    result['symbolic_residual'] = str(residual)
if importlib.util.find_spec('numpy') is not None:
    import numpy as np
    a = np.array([[2., 1.], [1., 3.]])
    b = np.array([1., 2.])
    residual = float(np.linalg.norm(a @ np.linalg.solve(a, b) - b))
    assert residual < 1e-12
    result['numpy_version'] = np.__version__
    result['linear_system_residual'] = residual
print(json.dumps(result))'''
            result = run([python, '-c', code], args.timeout, environment)
        elif not wolframscript:
            result = {'returncode': None, 'timed_out': False,
                      'stdout': '', 'stderr': 'wolframscript not found'}
        else:
            env = environment.copy()
            if kernel:
                env['WolframKernel'] = kernel
            code = ('TimeConstrained[Print[$Version];'
                    'Print["rational_sum=",1/3+1/6];'
                    'Print["symbolic_residual=",Simplify[D[Sin[x],x]-Cos[x]]];'
                    'If[1/3+1/6===1/2 && Simplify[D[Sin[x],x]-Cos[x]]===0,'
                    'Exit[0],Exit[2]],15,Exit[124]]')
            result = run([wolframscript, '-code', code], args.timeout, env)
        report['smoke'][backend] = result
        failed = failed or result['returncode'] != 0 or result['timed_out']
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
