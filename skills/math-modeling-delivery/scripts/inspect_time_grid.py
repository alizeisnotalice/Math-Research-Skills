#!/usr/bin/env python3
"""Inspect an elapsed-time column without changing the input (CSV or XLSX)."""
import argparse
import csv
from collections import Counter
from datetime import date, time
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import sys
from zipfile import BadZipFile


def number(value):
    if value is None or isinstance(value, (bool, date, time)):
        raise ValueError(f"Not a numeric elapsed time: {value!r}")
    try:
        result = Decimal(str(value).strip())
    except InvalidOperation as exc:
        raise ValueError(f"Not a numeric elapsed time: {value!r}") from exc
    if not result.is_finite():
        raise ValueError("Time and contract values must be finite")
    return result


def column_index(column, header):
    if column.isdigit():
        index = int(column) - 1
        if index < 0 or index >= len(header):
            raise ValueError("Column number is outside the header")
        return index
    matches = [i for i, value in enumerate(header) if str(value) == column]
    if len(matches) != 1:
        raise ValueError("Column header must match exactly once; otherwise use a 1-based number")
    return matches[0]


def read_column(path, column, sheet, header_row):
    if path.suffix.lower() == ".csv":
        if sheet is not None:
            raise ValueError("--sheet only applies to XLSX")
        with path.open(encoding="utf-8-sig", newline="") as handle:
            rows = csv.reader(handle)
            for _ in range(header_row - 1):
                next(rows, None)
            header = next(rows, None)
            if not header:
                raise ValueError("Header row is missing")
            index = column_index(column, header)
            values = []
            for row_number, row in enumerate(rows, header_row + 1):
                if not row or not any(value.strip() for value in row):
                    continue
                if index >= len(row):
                    raise ValueError(f"Missing time column on CSV row {row_number}")
                values.append((row_number, number(row[index])))
            return {"sheet": None, "header": header[index]}, values
    if path.suffix.lower() != ".xlsx":
        raise ValueError("Only CSV and XLSX are supported")
    try:
        from openpyxl import load_workbook
    except ImportError as exc:
        raise ValueError("XLSX readback requires openpyxl; CSV inspection uses only the standard library") from exc
    try:
        workbook = load_workbook(path, read_only=True, data_only=False)
    except KeyError as exc:
        raise ValueError(f"XLSX container is missing a required workbook member: {exc}") from exc
    try:
        if sheet is None:
            if len(workbook.sheetnames) != 1:
                raise ValueError("Specify --sheet for a multi-sheet workbook")
            sheet = workbook.sheetnames[0]
        if sheet not in workbook.sheetnames:
            raise ValueError("Worksheet does not exist")
        rows = workbook[sheet].iter_rows(min_row=header_row)
        header = next(rows, None)
        if not header:
            raise ValueError("Header row is missing")
        index = column_index(column, [cell.value for cell in header])
        values = []
        for row_number, row in enumerate(rows, header_row + 1):
            if not any(cell.value is not None for cell in row):
                continue
            if index >= len(row):
                raise ValueError(f"Missing time column on XLSX row {row_number}")
            cell = row[index]
            if cell.data_type in {"f", "e", "b", "d"} or cell.is_date:
                raise ValueError(f"Time cell on row {row_number} is a formula, error, boolean or date; resolve its semantics first")
            values.append((row_number, number(cell.value)))
        return {"sheet": sheet, "header": header[index].value}, values
    finally:
        workbook.close()


def inspect(values, factor, step, origin, tolerance, expected_first, expected_last, allow_final):
    if len(values) < 2:
        raise ValueError("At least two time records are needed to inspect sampling intervals")
    if step <= 0 or tolerance < 0 or tolerance >= step / 2:
        raise ValueError("Require step > 0 and 0 <= tolerance < step/2")
    if allow_final and expected_last is None:
        raise ValueError("An off-grid final row needs an explicitly supplied --expected-last-seconds")
    times = [value * factor for _, value in values]
    differences = [right - left for left, right in zip(times, times[1:])]
    issues = []
    def issue(kind, index):
        issues.append({"kind": kind, "row": values[index][0], "time_seconds": str(times[index])})
    final_exception = False
    for i, value in enumerate(times):
        offset = value - origin
        on_grid = abs(offset - (offset / step).to_integral_value() * step) <= tolerance
        final_ok = (allow_final and i == len(times) - 1 and i > 0
                    and abs(value - expected_last) <= tolerance
                    and 0 < value - times[i - 1] < step)
        if not on_grid:
            if final_ok:
                final_exception = True
            else:
                issue("off_grid", i)
        if i and differences[i - 1] <= 0:
            issue("non_increasing_time", i)
        elif i and abs(differences[i - 1] - step) > tolerance and not (not on_grid and final_ok):
            issue("unexpected_interval", i)
    if expected_first is not None and abs(times[0] - expected_first) > tolerance:
        issue("unexpected_first_time", 0)
    if expected_last is not None and abs(times[-1] - expected_last) > tolerance:
        issue("unexpected_last_time", len(times) - 1)
    return {"matches_supplied_grid_contract": not issues, "records": len(times),
            "first_seconds": str(times[0]), "last_seconds": str(times[-1]),
            "interval_counts_seconds": {str(delta): count for delta, count in Counter(differences).items()},
            "expected_step_seconds": str(step), "origin_seconds": str(origin),
            "tolerance_seconds": str(tolerance), "first_boundary_checked": expected_first is not None,
            "last_boundary_checked": expected_last is not None, "final_off_grid_row_accepted": final_exception,
            "issues_count": len(issues), "issues_first_20": issues[:20],
            "scope": "Only the selected time column and supplied contract are checked; units, completeness outside supplied boundaries, model correctness and other cells require separate evidence."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--column", required=True, help="Exact header or 1-based column number")
    parser.add_argument("--unit", required=True, choices=["s", "min", "h"], help="Actual unit of stored time values")
    parser.add_argument("--sheet")
    parser.add_argument("--header-row", type=int, default=1)
    parser.add_argument("--expected-step-seconds", required=True, type=number)
    parser.add_argument("--origin-seconds", type=number, default=Decimal(0))
    parser.add_argument("--tolerance-seconds", type=number, default=Decimal(0))
    parser.add_argument("--expected-first-seconds", type=number)
    parser.add_argument("--expected-last-seconds", type=number)
    parser.add_argument("--allow-final-off-grid", action="store_true")
    args = parser.parse_args()
    try:
        if args.header_row < 1:
            raise ValueError("--header-row must be positive")
        selected, values = read_column(args.file, args.column, args.sheet, args.header_row)
        report = inspect(values, Decimal({"s": 1, "min": 60, "h": 3600}[args.unit]),
                         args.expected_step_seconds, args.origin_seconds, args.tolerance_seconds,
                         args.expected_first_seconds, args.expected_last_seconds, args.allow_final_off_grid)
        report.update({"file": str(args.file), "selected_column": selected, "stored_unit": args.unit})
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["matches_supplied_grid_contract"] else 1
    except (ValueError, OSError, csv.Error, BadZipFile) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
