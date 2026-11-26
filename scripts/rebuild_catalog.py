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
          'research-specialists':'专题数学研究与证书','probability':'概率研究专题','literature':'文献检索与获取','writing':'论文写作、翻译与表达',
          'modeling':'数学建模竞赛','collaboration':'指定模型咨询'}
FAMILIES = {'a':'归一化、外放松与紧性','b':'对偶、矩问题与交换','c':'锥规划、SOS 与全局优化',
            'd':'输运、熵与自由能','e':'占用测度、Bellman 与停止','f':'Fourier、谱与平方函数',
            'g':'Carleson 与树结构','h':'中偏差与指数倾斜','i':'滤过、补偿与随机占用',
            'j':'非齐次跳跃过程','k':'随机场极值与集中','l':'计算搜索与严格证书',
            'm':'凸性、极点与选择','n':'凸几何、振荡与误差'}


SPECIALTY_FIELDS = {
    'euler-gamma-pade': {
        'label': '欧拉常数、Padé 与整数线性形式',
        'route': 'γ 的无理性、特殊值逼近、精确递推或有限 Padé/行列式证书。',
        'names': (
        'math-euler-constant-irrationality',
        'math-order-two-casoratian-audit',
        'math-prevost-hurwitz-pade-remainder',
        'math-euler-series-continued-fraction',
        'math-sondow-log-fractional-certificate',
        'math-gamma-continued-fraction-recurrence',
        'math-gamma-gregory-series-interval',
        'math-gamma-meijer-cmf',
        'math-gamma-multiple-laguerre-approximants',
        'math-openai-arithmetic-determinants',
        'math-alternating-reciprocal-criteria',
        'math-integer-linear-form-rates',
        'math-hankel-pade-certificates',
        'math-euler-maclaurin-quadrature-certificates',
        'math-harmonic-sum-recurrences',
        'math-zeta-polynomial-expansion-coefficients',
    )},
    'transcendence-diophantine-g-functions': {
        'label': '超越性、丢番图逼近与 G/Mahler 函数',
        'route': '代数独立、有效逼近、Mahler/G-函数或指数丢番图问题。',
        'names': (
        'math-exponential-order-reduction',
        'math-four-square-witness-certificates',
        'math-exponential-logarithm-algebraic-independence',
        'math-rational-logarithm-independence-gate',
        'math-algebraic-group-logarithm-distance',
        'math-baker-runge-height-gates',
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
        'math-parameterized-norm-form-certificates',
        'math-primary-pseudopolynomial-certificates',
        'math-syracuse-exact-words',
        'math-ax-schanuel-dimension-defect',
        'math-q-series-rational-approximants',
        'math-function-field-period-transcendence',
    )},
    'analytic-number-theory-special-functions': {
        'label': '解析数论、L 函数、模形式与特殊函数',
        'route': 'ζ/L 函数、模形式、MZV、特殊函数及其有限恒等式。',
        'names': (
        'math-dirichlet-l-value-span-scope',
        'math-hypergeometric-padic-prime-density',
        'math-modified-dirichlet-character-omega-bound',
        'math-modular-bootstrap-certification',
        'math-xi-theta-finite-certificates',
        'math-cmzv-rational-pullback',
        'math-cyclotomic-euler-t-parity',
        'math-motivic-euler-sum-unramifiedness',
        'math-selberg-riesz-criteria',
        'math-nevanlinna-functional-transcendence',
        'math-bessel-cross-product-recurrence',
        'math-modular-holonomic-telescoping',
        'math-dirichlet-l-derivative-sine-reduction',
        'math-mzv-newton-harmonic-relations',
        'math-zeta-arithmetic-estimates',
    )},
    'differential-difference-dynamics': {
        'label': '微分差分方程、递推与动力系统',
        'route': '有限递推、差分 Galois、可积系统、正交多项式或周期轨道。',
        'names': (
        'math-finite-cyclic-difference-pv',
        'math-double-elliptic-orbit-confinement',
        'math-semiclassical-orthogonal-deformations',
        'math-differential-operator-minimization',
        'math-linear-difference-hypertranscendence',
        'math-hofstadter-nested-recurrences',
        'math-recurrence-finite-screening',
        'math-local-bottcher-formal-conjugacy',
        'math-lienard-half-arc-matching',
    )},
    'analysis-geometry-pde': {
        'label': '调和、几何与泛函分析及 PDE',
        'route': '极大算子、Fourier/谱、度量几何、热核、共形或几何 PDE。',
        'names': (
        'math-strip-poisson-smoothing',
        'math-conformal-dimension-perron-brackets',
        'math-subanalytic-preparation',
        'math-asymptotic-midpoint-moduli',
        'math-conformal-domain-estimates',
        'math-tube-maximal-transfer',
        'math-centered-cube-endpoint-budget',
        'math-hbl-finite-presentation',
        'math-torus-packet-spectral-density',
        'math-cat0-inductive-barycenters',
        'math-geometric-pde-reductions',
        'math-lattice-heat-asymptotics',
    )},
    'algebraic-arithmetic-geometry': {
        'label': '代数几何、模空间、p-adic 与非阿基米德几何',
        'route': '除子、Hodge/period、特殊点、模曲线、p-adic 或非阿基米德资料。',
        'names': (
        'math-ladic-level-triviality-gate',
        'math-fermat-hodge-lattice-quotients',
        'math-geometric-g-function-special-points',
        'math-likely-intersections-density',
        'math-modular-unlikely-intersections',
        'math-padic-abelian-intersection-bounds',
        'math-special-point-bound-gates',
        'math-holomorphic-local-to-global-transfer',
        'math-ag-divisor-intersection-ledger',
        'math-nonarchimedean-analytic-transfer',
        'math-weil-deligne-purity-lfactor',
    )},
    'algebra-representation-operator-cohomology': {
        'label': '代数、表示论、算子代数与上同调',
        'route': '有限代数、群与表示、算子代数、链复形或转移证书。',
        'names': (
        'math-mixed-determinant-border-certificates',
        'math-heisenberg-group-determinant-certificates',
        'math-symmetric-polynomial-ratio-certificates',
        'math-nonnegative-matrix-path-certificates',
        'math-finite-nonassociative-algebra-audits',
        'math-algebraic-transfer-certificates',
        'math-cohomological-transfer',
        'math-f2-group-ring-cancellation',
        'math-free-group-presentation-traces',
        'math-operator-algebra-certificates',
        'math-projective-induction-cocycle-certificates',
    )},
    'discrete-combinatorics-games': {
        'label': '图论、组合、离散几何与博弈',
        'route': '有限图、计数、permanent、半群、概率组合或有限博弈证书。',
        'names': (
        'math-lattice-box-manhattan-ordering',
        'math-rees-zero-complete-mappings',
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
        'math-bimatrix-kite-mixing',
        'math-edge-deck-reconstruction-audit',
        'math-finite-graph-family-witnesses',
        'math-honeycomb-finite-boundary-flux',
        'math-clique-free-random-multiplier',
        'math-grid-piecewise-translation-embedding',
        'math-three-strip-token-bound',
    )},
    'complexity-tensor-transfer': {
        'label': '复杂性、张量与离散证明迁移',
        'route': '通信复杂性、张量复杂性或已命名研究项目的有限迁移接口。',
        'names': (
        'euclidean-tensor-geometry',
        'math-discrete-proof-transfer',
        'math-logrank-rectangle-rank-halving',
    )},
}
SPECIALIST_TOPICS = {field['label']: field['names'] for field in SPECIALTY_FIELDS.values()}
SPECIALTY_BY_NAME = {
    name: {'key': key, 'label': field['label']}
    for key, field in SPECIALTY_FIELDS.items()
    for name in field['names']
}
if len(SPECIALTY_BY_NAME) != sum(len(field['names']) for field in SPECIALTY_FIELDS.values()):
    raise ValueError('a specialist skill appears in more than one specialty field')
SPECIALIST_NAMES = set(SPECIALTY_BY_NAME)


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
        if item['category']=='research-specialists':
            item['specialty'] = SPECIALTY_BY_NAME[name]['key']
            item['specialty_label'] = SPECIALTY_BY_NAME[name]['label']
        if name in ALIASES: item['alias_for']=ALIASES[name]
        if name in RUNTIME_SKILLS: item['requires'] = RUNTIME_SKILLS[name]
        skills.append(item)
    counts = dict(Counter(s['category'] for s in skills))
    specialty_fields = [
        {'key': key, 'label': field['label'], 'route': field['route'],
         'count': len(field['names'])}
        for key, field in SPECIALTY_FIELDS.items()
    ]
    write_json(ROOT/'catalog/skills.json',{'schema_version':1,'entry_skill':'math-research',
               'categories':LABELS,'specialty_fields':specialty_fields,
               'counts':counts,'skills':skills})
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
            lines.extend(['按研究对象选专项路线时见[专题数学方法](research-specialists.md)。专项索引按稳定领域键分组，单项技能的具体假设仍以其技能文件和原文为准。',''])
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
    specialists = ['# 专题数学方法', '', '按对象找到可调用的证明构件和精确检查器。先核对输入及来源的适用范围。领域键稳定，用于路由和机器索引，不替代单项技能的适用条件。']
    for field_key, field in SPECIALTY_FIELDS.items():
        specialists.extend(['', f'<a id="{field_key}"></a>', '', f'## {field["label"]}', '', field['route'], ''])
        names = field['names']
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
