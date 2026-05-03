# Human audit result workflow

This file describes what to do after the manual audit forms are returned.

## Expected inputs

- `docs/human_quality_audit_fillable.xlsx`, if one reviewer fills the Excel form.
- `docs/human_quality_audit_reviewer1.csv` and `docs/human_quality_audit_reviewer2.csv`, if two reviewers work independently.
- `quality_report/human_audit_contact_sheets/audit_*.png`, the reviewed images.

## Single-reviewer path

1. Export the completed Excel form as CSV, or fill `docs/human_quality_audit_samples.csv` directly.
2. Run `scripts/analyze_human_audit_results.py` on the completed CSV.
3. Review the generated summary and issue counts.
4. Decide how to handle `reject` samples.

## Two-reviewer path

1. Give each reviewer an independent copy of the audit table.
2. Convert both completed tables to CSV.
3. Run `scripts/compare_human_audits.py` with reviewer 1 and reviewer 2 files.
4. Fill `human_quality_audit_adjudication_template.csv` for disagreement rows.
5. Use the adjudicated result as the final manual-audit record.

## Decision policy

- `accept`: retain.
- `flag`: retain by default, but summarize issue type in the audit report.
- `reject`: remove or replace before final public benchmark release, especially if the sample is in val/test.

## Outputs to generate after review

- `quality_report/human_quality_audit_summary.csv`
- `quality_report/human_quality_audit_report.md`
- updated Dataset Card audit section
- updated checksums if any release-package files change
