#!/usr/bin/env python3
"""Run only our MATLAB batch session, record exit, terminate our group on timeout."""
import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import time


def is_matlab_main(command):
    return Path(command).name in ('MATLAB','MATLAB_maca64','MATLAB_maci64')


def matlab_pids():
    rows = subprocess.check_output(["ps", "-axo", "pid=,comm="], text=True).splitlines()
    result=[]
    for row in rows:
        fields=row.strip().split(None,1)
        if len(fields)==2 and is_matlab_main(fields[1]): result.append(int(fields[0]))
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--matlab", type=Path, default=Path("/Applications/MATLAB_R2026b.app/bin/matlab"))
    p.add_argument("--script", type=Path, required=True)
    p.add_argument("--report", type=Path, required=True)
    p.add_argument("--log", type=Path, required=True)
    p.add_argument("--timeout", type=int, default=180)
    a = p.parse_args()
    if not Path("/Volumes/data").is_mount():
        raise RuntimeError("data volume is not mounted; no system-disk fallback.")
    if not a.matlab.is_file() or not a.script.is_file() or a.timeout < 1:
        p.error("Existing MATLAB and script paths, and positive timeout, are required.")
    if not a.log.is_absolute() or not a.report.is_absolute():
        p.error("Use absolute paths for log and report.")
    a.log.parent.mkdir(parents=True, exist_ok=True)
    a.report.parent.mkdir(parents=True, exist_ok=True)
    before = matlab_pids()
    escaped = str(a.script.resolve()).replace("'", "''")
    started = time.perf_counter()
    timed_out = False
    with a.log.open("w") as log:
        proc = subprocess.Popen([str(a.matlab), "-batch", "run('" + escaped + "')"],
            cwd=a.script.parent, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            code = proc.wait(timeout=a.timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                code = proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                code = proc.wait(timeout=10)
    # The launcher normally waits for MATLAB, but explicitly check our process group.
    processes = subprocess.check_output(["ps", "-axo", "pid=,pgid=,comm="], text=True).splitlines()
    group_alive = []
    for row in processes:
        fields = row.strip().split(None, 2)
        if len(fields) == 3 and int(fields[1]) == proc.pid:
            group_alive.append({"pid": int(fields[0]), "command": fields[2]})
    main_alive = [r for r in group_alive if is_matlab_main(r['command'])]
    if main_alive:
        # Only clean up a still-running batch computation, not normal license helpers.
        os.killpg(proc.pid, signal.SIGTERM)
    after = matlab_pids()
    report = {"ok": code == 0 and not timed_out and not main_alive,
        "returncode": code, "timed_out": timed_out, "launcher_pid": proc.pid,
        "elapsed_seconds": time.perf_counter() - started,
        "matlab_pids_before": before, "matlab_pids_after": after,
        "own_matlab_main_remaining_at_exit": main_alive,
        "own_group_auxiliaries_at_exit": [r for r in group_alive if r not in main_alive],
        "script": str(a.script.resolve()), "log": str(a.log)}
    a.report.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report))
    return 0 if report["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
