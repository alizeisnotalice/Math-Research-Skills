import importlib.util
from pathlib import Path
import sys
import unittest


path = Path(__file__).resolve().parents[1] / "skills/math-research/scripts/find_literature_source.py"
spec = importlib.util.spec_from_file_location("literature_lookup", path)
lookup = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = lookup
spec.loader.exec_module(lookup)

SHA = "a" * 64
FIRST = "2026-11-26T18:00:00+08:00"
SECOND = "2026-11-27T09:00:00+08:00"


def source(name, *lines, collection="historical"):
    header = ["## Example study", "- 原件。SHA-256 " + SHA + "。"]
    return next(lookup.section_occurrences(Path(name), header + list(lines), collection, "- 原件"))


class ReviewRecordsTests(unittest.TestCase):
    def test_latest_dated_review_controls_filter_and_keeps_old_location(self):
        old = source("old.md", "- 待核。依赖待提供。", "- 依赖复核。旧范围。")
        interim = source("interim.md", f"- 复核记录。{FIRST}。candidate。dependency。")
        current = source("current.md", f"- 复核记录。{SECOND}。existing。statement。")
        occurrences = [current, old, interim]
        result = lookup.search_occurrences(occurrences, "", [], None, "existing")
        self.assertEqual(result[SHA][0], current)
        self.assertCountEqual(result[SHA], occurrences)
        self.assertEqual(lookup.summarize(result, occurrences)["historical"]["statuses"], {"existing": 1})
        self.assertEqual(lookup.location_fields(old, current)["current"], False)
        self.assertEqual(lookup.location_fields(current, current)["review_scope"], "statement")

    def test_explicit_adoption_is_separate_from_current_label(self):
        review = f"- 复核记录。{FIRST}。adopted-local。component。"
        unsupported = source("only-label.md", review, collection="recent")
        callable_record = source("explicit-link.md", review, "- 已采用构件。见方法。", collection="recent")
        self.assertFalse(lookup.search_occurrences([unsupported], "", [], None, "adopted"))
        self.assertIn(SHA, lookup.search_occurrences([callable_record], "", [], None, "adopted"))

    def test_multiple_status_filters_combine_current_dispositions_and_adoptions(self):
        candidate = source("candidate.md", f"- 复核记录。{FIRST}。candidate。dependency。")
        held = source("held.md", f"- 复核记录。{FIRST}。held。dependency。", collection="recent")
        usable = source("usable.md", f"- 复核记录。{FIRST}。scoped-reference。statement。",
                        "- 已采用构件。见方法。", collection="supplemental")
        occurrences = [candidate, held, usable]
        result = lookup.search_occurrences(occurrences, "", [], None, ["candidate", "held"])
        self.assertCountEqual(result[SHA], [candidate, held])
        self.assertCountEqual(
            lookup.search_occurrences(occurrences, "", [], None, ["held", "adopted"])[SHA],
            [held, usable],
        )
        self.assertEqual(lookup.search_occurrences(occurrences, "", [], None, "existing")[SHA], [usable])

    def test_equal_timestamp_with_conflicting_dispositions_is_rejected(self):
        old = source("one.md", f"- 复核记录。{FIRST}。hold。dependency。")
        new = source("two.md", f"- 复核记录。{FIRST}。existing。statement。")
        with self.assertRaisesRegex(ValueError, "conflicting review records"):
            lookup.current_records([old, new])

    def test_review_requires_time_zone(self):
        with self.assertRaisesRegex(ValueError, "requires a time zone"):
            source("invalid.md", "- 复核记录。2026-11-26T12:00:00。citation。citation。")


if __name__ == "__main__":
    unittest.main()
