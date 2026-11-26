import itertools
import json
from pathlib import Path
import runpy
import unittest


SKILLS = Path(__file__).resolve().parents[1] / "skills"


class SkillExampleContracts(unittest.TestCase):
    def test_petal_join_matches_direct_enumeration_including_empty_outer_graph(self):
        script = SKILLS / "math-petal-join-domination-polynomial/scripts/check_petal_join.py"
        check = runpy.run_path(str(script))["check"]
        for order in range(5):
            possible_edges = list(itertools.combinations(range(order), 2))
            for mask in range(1 << len(possible_edges)):
                edges = [edge for i, edge in enumerate(possible_edges) if mask >> i & 1]
                for clique, copies in itertools.product((1, 2), range(3)):
                    report = check({"n": order, "edges": edges}, clique, copies)
                    self.assertTrue(report["exact_match"], (order, edges, clique, copies))
                    if order * copies == 0:
                        self.assertEqual(report["formula"], [0, 1] if clique == 1 else [0, 2, 1])

    def test_basic_a3_terrace_reports_its_directed_status_separately(self):
        skill = SKILLS / "math-finite-permutation-terrace-certificates"
        checker = runpy.run_path(str(skill / "scripts/check_terrace.py"))["verify_terrace"]
        example = json.loads((skill / "examples/a3-positive.json").read_text())
        report = checker(example["degree"], [tuple(row) for row in example["rows"]])
        self.assertEqual(report["condition"], "basic-terrace-inverse-pairs")
        self.assertFalse(report["directed"])
        self.assertEqual(report["consecutive_quotients"], 2)


if __name__ == "__main__":
    unittest.main()
