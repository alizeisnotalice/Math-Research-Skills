#!/usr/bin/env python3
"""Run a bounded Wolfram script using data-volume paclets."""
import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import time


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--kernel",type=Path,default=Path("/Applications/Wolfram.app/Contents/MacOS/WolframKernel"))
    p.add_argument("--pacletbase",type=Path,default=Path("/Volumes/data/CodexData/runtimes/wolfram-paclets"))
    p.add_argument("--script",type=Path,required=True)
    p.add_argument("--report",type=Path,required=True)
    p.add_argument("--log",type=Path,required=True)
    p.add_argument("--timeout",type=int,default=180)
    a=p.parse_args()
    if not Path('/Volumes/data').is_mount(): raise RuntimeError('data volume not mounted.')
    if not a.kernel.is_file() or not a.script.is_file() or a.timeout<1:
        p.error('Existing kernel/script and positive timeout required.')
    if any(not x.is_absolute() for x in (a.pacletbase,a.report,a.log)):
        p.error('Absolute paths required.')
    for d in (a.pacletbase,a.report.parent,a.log.parent): d.mkdir(parents=True,exist_ok=True)
    started=time.perf_counter(); timed_out=False
    with a.log.open('w') as log:
        proc=subprocess.Popen([str(a.kernel),'-pacletbase',str(a.pacletbase),'-script',str(a.script.resolve())],
            cwd=a.script.parent,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        try: code=proc.wait(timeout=a.timeout)
        except subprocess.TimeoutExpired:
            timed_out=True; os.killpg(proc.pid,signal.SIGTERM)
            try: code=proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid,signal.SIGKILL); code=proc.wait(timeout=10)
    r={'ok':code==0 and not timed_out,'returncode':code,'timed_out':timed_out,
       'kernel_pid':proc.pid,'process_reaped':proc.poll() is not None,
       'elapsed_seconds':time.perf_counter()-started,'pacletbase':str(a.pacletbase),
       'script':str(a.script.resolve()),'log':str(a.log)}
    a.report.write_text(json.dumps(r,indent=2)+'\n'); print(json.dumps(r))
    return 0 if r['ok'] else 2


if __name__=='__main__': raise SystemExit(main())
