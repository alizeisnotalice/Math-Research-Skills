#!/usr/bin/env python3
"""Compare useful repeated Markov propagation with arrays kept on CPU/GPU."""
import argparse,json,os,time,statistics
from pathlib import Path
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='0'
import numpy as np
import torch


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--n',type=int,default=1024)
    p.add_argument('--steps',type=int,default=16)
    p.add_argument('--report',type=Path,required=True)
    a=p.parse_args()
    if not 32<=a.n<=2048 or not 1<=a.steps<=64: p.error('Use n=32..2048, steps=1..64.')
    if not torch.backends.mps.is_available(): raise RuntimeError('Actual MPS is required for this comparison.')
    rng=np.random.default_rng(20261116)
    x=rng.random((a.n,a.n),dtype=np.float32); x/=x.sum(axis=1,keepdims=True)
    transition=rng.random((a.n,a.n),dtype=np.float32); transition/=transition.sum(axis=1,keepdims=True)
    def numpy_run():
        y=x
        for _ in range(a.steps):y=y@transition
        return y
    def torch_cpu_run(threads):
        torch.set_num_threads(threads)
        y=torch.from_numpy(x); b=torch.from_numpy(transition)
        for _ in range(a.steps):y=y@b
        return y.numpy()
    def mps_run():
        y=torch.from_numpy(x).to('mps');b=torch.from_numpy(transition).to('mps')
        for _ in range(a.steps):y=y@b
        torch.mps.synchronize()
        assert y.device.type=='mps'
        return y.cpu().numpy().copy()
    choices=[('numpy-cpu',numpy_run)]
    for threads in sorted({min(t,os.cpu_count() or 1) for t in (1,2,4,8,os.cpu_count() or 1)}):
        choices.append((f'torch-cpu-{threads}',lambda t=threads:torch_cpu_run(t)))
    choices.append(('mps',mps_run))
    rows=[]; outputs={}
    with torch.inference_mode():
        for name,fn in choices:
            fn(); times=[]
            for _ in range(3):
                start=time.perf_counter(); y=fn(); times.append(time.perf_counter()-start)
            rows.append({'backend':name,'median_seconds':statistics.median(times),'runs_seconds':times})
            outputs[name]=y[[0,a.n//3,2*a.n//3,a.n-1],:].astype(float)
    reference=x[[0,a.n//3,2*a.n//3,a.n-1],:].astype(float)
    for _ in range(a.steps):reference=reference@transition.astype(float)
    for row in rows:
        error=np.abs(outputs[row['backend']]-reference)
        row['checked_rows']=4;row['max_abs_error']=float(error.max())
        row['passed']=bool(np.all(error<=1e-7+5e-4*np.abs(reference)))
    cpu=min((r for r in rows if r['backend']!='mps'),key=lambda r:r['median_seconds'])
    gpu=next(r for r in rows if r['backend']=='mps')
    winner='mps' if gpu['passed'] and gpu['median_seconds']<.9*cpu['median_seconds'] else cpu['backend']
    report={'ok':all(r['passed'] for r in rows),'n':a.n,'steps':a.steps,'dtype':'float32',
        'seed':20261116,'rows':rows,'selected':winner,'best_cpu':cpu['backend'],
        'gpu_vs_best_cpu_speedup':cpu['median_seconds']/gpu['median_seconds'],
        'timing_scope':'warm process, one input upload + all propagation steps + final download; no per-step transfer; excludes interpreter import/calibration/reference',
        'verification':'four complete rows vs CPU float64 propagation; numerical evidence, not full-array proof'}
    a.report.parent.mkdir(parents=True,exist_ok=True)
    a.report.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
    return 0 if report['ok'] else 2


if __name__=='__main__':raise SystemExit(main())
