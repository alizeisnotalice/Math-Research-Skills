from pathlib import Path
import json, sys, hashlib
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'.runtime'))
import sympy as sp

c,u,v = sp.symbols('c u v', nonnegative=True)
identity = sp.expand(2*(c+u)*(c+v)-c*(2*c+u+v))
assert identity == c*u+c*v+2*u*v
spectra=[]
for m in range(1,5):
    size=2**m; P=sp.zeros(size)
    for x in range(size):
        for coordinate in range(m):
            P[x,x]+=sp.Rational(1,2*m)
            P[x,x^(1<<coordinate)]+=sp.Rational(1,2*m)
    values=(sp.eye(size)-P).eigenvals()
    gap=min(value for value in values if value>0)
    assert gap==sp.Rational(1,m)
    spectra.append({'dimension':m,'gap':str(gap),'multiplicities':{str(k):v for k,v in values.items()}})
pdf=ROOT/'workers/W04/papers/LPW2017.pdf'
out={'source':str(pdf.relative_to(ROOT)),'source_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
     'source_physical_pages':[231,239,240],'source_printed_pages':[215,223,224],
     'harmonic_mean_numerator_identity':str(identity),'uniform_cube_finite_checks':spectra,
     'independently_derived_coefficient':'M Mstar exp(2 beta Delta M)',
     'source_stated_coefficient':'4 M^2 Mstar exp(2 beta Delta (M+1))',
     'scope':'Finite exact checks; universal proof and restricted hypotheses in adjacent note. Independent R02 review required before adoption.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checked_cube_dimensions':[1,2,3,4],'exact_gaps':[r['gap'] for r in spectra],'harmonic_identity':str(identity)}))
