#!/usr/bin/env python3
"""Refresh discovery indexes and checksums after deliberate skill edits."""
from collections import Counter
import json
from pathlib import Path
import re
import yaml
from skill_common import digest, write_json

ROOT = Path(__file__).resolve().parents[1]
ALIASES = {'mathematica-research':'mathematica-math',
           'literature-download':'literature-search-download',
           'pdf-paper-translate':'academic-paper-translator'}
RUNTIME_SKILLS = {
    'math-euler-constant-irrationality': [
        'math-openai-arithmetic-determinants',
        'math-prevost-hurwitz-pade-remainder',
        'math-order-two-casoratian-audit',
        'math-euler-series-continued-fraction',
        'math-alternating-reciprocal-criteria',
        'math-sondow-log-fractional-certificate',
        'math-gamma-multiple-laguerre-approximants',
        'math-gamma-meijer-cmf',
        'math-gamma-continued-fraction-recurrence',
        'math-gamma-gregory-series-interval',
        'math-integer-linear-form-rates',
        'math-hankel-pade-certificates',
        'math-l03-rational-and-interval-certificates',
    ],
    'math-research': ['math-tool-router'],
    'probability-martingale-stopping': ['probability-measure-convergence'],
    'probability-bernoulli-extremal-orders': ['probability-moment-polynomial-duality'],
    'math-geometric-pde-reductions': ['python-math'],
    'math-l03-rational-and-interval-certificates': ['python-math'],
    'math-l19-coordinate-ring-certificates': ['python-math'],
    'math-tool-router': [
        'python-math', 'mathematica-math', 'matlab-plotting',
        'local-hybrid-math', 'remote-math-compute', 'ipad-math-node',
    ],
}
LABELS = {'orchestration':'研究总入口','tools':'计算与绘图工具','methods':'数学方法（A–N）',
          'research-specialists':'专项研究核验','probability':'概率研究专题','literature':'文献检索与获取','writing':'论文写作、翻译与表达',
          'modeling':'数学建模竞赛','collaboration':'指定模型咨询'}
FAMILIES = {'a':'归一化、外放松与紧性','b':'对偶、矩问题与交换','c':'锥规划、SOS 与全局优化',
            'd':'输运、熵与自由能','e':'占用测度、Bellman 与停止','f':'Fourier、谱与平方函数',
            'g':'Carleson 与树结构','h':'中偏差与指数倾斜','i':'滤过、补偿与随机占用',
            'j':'非齐次跳跃过程','k':'随机场极值与集中','l':'计算搜索与严格证书',
            'm':'凸性、极点与选择','n':'凸几何、振荡与误差'}


SPECIALIST_TOPICS = {
    '欧拉常数、丢番图逼近与算术': (
        'math-exponential-logarithm-algebraic-independence',
        'math-algebraic-group-logarithm-distance',
        'math-baker-runge-height-gates',
        'math-cmzv-rational-pullback',
        'math-cyclotomic-euler-t-parity',
        'math-differential-operator-minimization',
        'math-elliptic-quasielliptic-function-independence',
        'math-exponential-algebraic-methods',
        'math-fibonacci-valuation-reductions',
        'math-finite-field-formal-series-congruences',
        'math-g-function-restricted-approximation',
        'math-gfunction-representability-obstructions',
        'math-lacunary-recurrence-transcendence',
        'math-mahler-purity-filtration',
        'math-mahler-system-admission',
        'math-mixed-littlewood-pseudoadic',
        'math-motivic-euler-sum-unramifiedness',
        'math-parameterized-norm-form-certificates',
        'math-primary-pseudopolynomial-certificates',
        'math-syracuse-exact-words',
        'math-zeta-polynomial-expansion-coefficients',
        'math-ax-schanuel-dimension-defect',
        'math-hofstadter-nested-recurrences',
        'math-order-two-casoratian-audit',
        'math-prevost-hurwitz-pade-remainder',
        'math-q-series-rational-approximants',
        'math-modular-holonomic-telescoping',
        'math-harmonic-sum-recurrences',
        'math-dirichlet-l-derivative-sine-reduction',
        'math-euler-series-continued-fraction',
        'math-mzv-newton-harmonic-relations',
        'math-zeta-arithmetic-estimates',
        'math-function-field-period-transcendence',
        'math-euler-constant-irrationality',
        'math-sondow-log-fractional-certificate',
        'math-gamma-continued-fraction-recurrence',
        'math-gamma-gregory-series-interval',
        'math-gamma-meijer-cmf',
        'math-gamma-multiple-laguerre-approximants',
        'math-openai-arithmetic-determinants',
        'math-alternating-reciprocal-criteria',
        'math-integer-linear-form-rates',
        'math-hankel-pade-certificates',
    ),
    '调和分析、动力系统与几何方程': (
        'math-double-elliptic-orbit-confinement',
        'math-selberg-riesz-criteria',
        'math-strip-poisson-smoothing',
        'math-semiclassical-orthogonal-deformations',
        'math-nevanlinna-functional-transcendence',
        'math-conformal-dimension-perron-brackets',
        'math-bessel-cross-product-recurrence',
        'math-subanalytic-preparation',
        'math-asymptotic-midpoint-moduli',
        'math-conformal-domain-estimates',
        'math-tube-maximal-transfer',
        'math-centered-cube-endpoint-budget',
        'math-euler-maclaurin-quadrature-certificates',
        'math-hbl-finite-presentation',
        'math-torus-packet-spectral-density',
        'math-cat0-inductive-barycenters',
        'math-geometric-pde-reductions',
        'math-lattice-heat-asymptotics',
        'math-lienard-half-arc-matching',
    ),
    '算子代数、上同调与代数几何': (
        'math-fermat-hodge-lattice-quotients',
        'math-geometric-g-function-special-points',
        'math-heisenberg-group-determinant-certificates',
        'math-likely-intersections-density',
        'math-modular-unlikely-intersections',
        'math-padic-abelian-intersection-bounds',
        'math-special-point-bound-gates',
        'math-linear-difference-hypertranscendence',
        'math-symmetric-polynomial-ratio-certificates',
        'math-nonnegative-matrix-path-certificates',
        'math-finite-nonassociative-algebra-audits',
        'math-holomorphic-local-to-global-transfer',
        'math-algebraic-transfer-certificates',
        'math-ag-divisor-intersection-ledger',
        'math-cohomological-transfer',
        'math-f2-group-ring-cancellation',
        'math-nonarchimedean-analytic-transfer',
        'math-operator-algebra-certificates',
        'math-projective-induction-cocycle-certificates',
        'math-weil-deligne-purity-lfactor',
    ),
    '图、组合、博弈与复杂性': (
        'math-average-degree-tree-embedding',
        'math-finite-permutation-terrace-certificates',
        'math-graph-spectral-moment-certificates',
        'math-permanent-inequality-contracts',
        'math-petal-join-domination-polynomial',
        'math-regular-graph-low-induced-edge-count',
        'math-unfair-polynomial-trinomial-factors',
        'math-two-generator-graded-semigroup-certificates',
        'math-one-special-parking-equality',
        'math-cycle-weighted-permanent',
        'math-graded-character-order',
        'math-quantum-permanent-score',
        'math-cycle-type-likelihood-bounds',
        'euclidean-tensor-geometry',
        'math-discrete-proof-transfer',
        'math-bimatrix-kite-mixing',
        'math-logrank-rectangle-rank-halving',
        'math-edge-deck-reconstruction-audit',
        'math-honeycomb-finite-boundary-flux',
        'math-clique-free-random-multiplier',
        'math-grid-piecewise-translation-embedding',
        'math-three-strip-token-bound',
    ),
}
SPECIALIST_NAMES = {name for group in SPECIALIST_TOPICS.values() for name in group}


def category(name):
    if name == 'math-research': return 'orchestration'
    if re.match(r'math-[a-n]\d\d-',name): return 'methods'
    if name in SPECIALIST_NAMES:
        return 'research-specialists'
    if name.startswith('probability-'): return 'probability'
    if name.startswith('math-modeling-'): return 'modeling'
    if name in {'math-tool-router','local-hybrid-math','python-math','mathematica-math','mathematica-research','matlab-plotting','remote-math-compute','ipad-math-node'}: return 'tools'
    if name in {'academic-literature-search','cnki-search','literature-download','literature-search-download'}: return 'literature'
    if name == 'astra-delegate': return 'collaboration'
    return 'writing'


def frontmatter(path):
    text = path.read_text(encoding='utf-8')
    match = re.match(r'^---\n(.*?)\n---(?:\n|$)',text,re.S)
    if not match: raise ValueError('missing frontmatter: '+str(path))
    data = yaml.safe_load(match.group(1))
    if not isinstance(data,dict): raise ValueError('invalid frontmatter: '+str(path))
    return data,text[match.end():]


def main():
    skills = []
    for entry in sorted((ROOT/'skills').glob('*/SKILL.md')):
        data,body = frontmatter(entry)
        name = data['name']
        if name != entry.parent.name: raise ValueError('name mismatch: '+str(entry))
        heading = re.search(r'^# (.+)$',body,re.M)
        item = {'name':name,'title':heading.group(1) if heading else name,
                'description':data['description'].strip(),'category':category(name),
                'path':str(entry.relative_to(ROOT))}
        if item['category']=='methods': item['family']=name[5]
        if name in ALIASES: item['alias_for']=ALIASES[name]
        if name in RUNTIME_SKILLS: item['requires'] = RUNTIME_SKILLS[name]
        skills.append(item)
    counts = dict(Counter(s['category'] for s in skills))
    write_json(ROOT/'catalog/skills.json',{'schema_version':1,'entry_skill':'math-research',
               'categories':LABELS,'counts':counts,'skills':skills})
    index = ['# 数学研究技能目录','',f'共 {len(skills)} 个可调用入口。目录按职责分类，保留原技能名。标有兼容入口的技能转入对应主流程。','']
    for key,label in LABELS.items():
        index += ['## '+label,'','| 技能 | 用途 |','| --- | --- |']
        for item in skills:
            if item['category']!=key: continue
            alias = '（兼容 → '+item['alias_for']+'）' if item.get('alias_for') else ''
            index.append(f'| [{item["name"]}](../{item["path"]}){alias} | {item["description"].replace("|"," / ")} |')
        index.append('')
    (ROOT/'catalog/README.md').write_text('\n'.join(index))
    for kind,filename,title in [('methods','math-methods.md','数学方法索引'),('probability','probability.md','概率研究专题索引')]:
        lines=['# '+title,'','先检索当前问题的对象与方法，只读取相关技能。以下描述用于选路，具体定理与假设以技能及原文为准。','']
        if kind == 'methods':
            lines.extend(['离散研究、算术逼近和专门的证明核验见[专项数学方法](research-specialists.md)。',''])
        if kind == 'probability':
            lines.extend(['先核对技能中适用的来源卡。候选、待审和研究专用分支可用于检查假设与证据；正式引用或采用结论时应满足当前版本的来源范围。见[来源核对](source-review.md)。',''])
        previous = None
        for item in skills:
            if item['category']!=kind: continue
            family = item.get('family')
            if family and family != previous:
                lines += ['## '+family.upper()+' · '+FAMILIES[family],'']; previous=family
            lines += [f'- [{item["name"]}](../../{item["name"]}/SKILL.md)：{item["description"]}']
        (ROOT/'skills/math-research/references'/filename).write_text('\n'.join(lines)+'\n')
    by_name = {item['name']: item for item in skills}
    specialists = ['# 专项数学方法', '', '按对象找到可调用的证明构件和精确检查器。先核对输入及来源的适用范围。']
    for topic, names in SPECIALIST_TOPICS.items():
        specialists.extend(['', f'## {topic}', ''])
        for name in names:
            item = by_name[name]
            specialists.append(f'- [{name}](../../{name}/SKILL.md) · {item["description"]}')
    (ROOT / 'skills/math-research/references/research-specialists.md').write_text('\n'.join(specialists) + '\n')
    files = [{'path':str(p.relative_to(ROOT)),'sha256':digest(p),'bytes':p.stat().st_size,
              'mode':0o755 if p.stat().st_mode & 0o111 else 0o644}
             for p in sorted((ROOT/'skills').rglob('*')) if p.is_file()]
    write_json(ROOT/'catalog/skill-files.json',{'schema_version':1,'files':files})
    print(json.dumps({'skills':len(skills),'files':len(files),'counts':counts},ensure_ascii=False))


if __name__=='__main__': main()
