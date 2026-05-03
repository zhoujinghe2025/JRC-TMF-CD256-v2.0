#!/usr/bin/env python3
"""Summarize completed human audit results for JRC-TMF-CD256.

Usage:
  python scripts/analyze_human_audit_results.py --input docs/human_quality_audit_samples.csv --out-dir quality_report/human_audit_final
"""
import argparse, csv, json
from collections import Counter, defaultdict
from pathlib import Path

STATUS = {'accept','flag','reject'}
FIELDS = ['audit_status','visual_quality','label_alignment','cloud_shadow_issue','water_issue','boundary_confidence']

def read_rows(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def counter(rows, field):
    return Counter((r.get(field) or '').strip() or 'blank' for r in rows)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--out-dir', required=True)
    args = ap.parse_args()
    rows = read_rows(args.input)
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    reviewed = [r for r in rows if (r.get('audit_status') or '').strip()]
    invalid = [r for r in reviewed if r.get('audit_status') not in STATUS]
    summary = {
        'input': args.input,
        'total_rows': len(rows),
        'reviewed_rows': len(reviewed),
        'invalid_status_rows': len(invalid),
        'field_counts': {f: dict(counter(rows, f)) for f in FIELDS},
        'sample_type_by_status': {},
        'split_by_status': {},
        'source_by_status': {},
    }
    for group_field, out_key in [('sample_type','sample_type_by_status'), ('split','split_by_status'), ('source','source_by_status')]:
        table = defaultdict(Counter)
        for r in reviewed:
            table[r.get(group_field,'blank')][r.get('audit_status','blank')] += 1
        summary[out_key] = {k: dict(v) for k,v in sorted(table.items())}
    (out/'human_quality_audit_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    with (out/'human_quality_audit_summary.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['section','key','value'])
        w.writerow(['overall','total_rows',len(rows)])
        w.writerow(['overall','reviewed_rows',len(reviewed)])
        w.writerow(['overall','invalid_status_rows',len(invalid)])
        for field in FIELDS:
            for k,v in summary['field_counts'][field].items():
                w.writerow([field,k,v])
    status_counts = counter(rows, 'audit_status')
    report = ['# Human quality audit report', '', f'- Input: `{args.input}`', f'- Total rows: {len(rows)}', f'- Reviewed rows: {len(reviewed)}', f'- Invalid status rows: {len(invalid)}', '']
    report.append('## Status counts')
    report.append('')
    for k,v in status_counts.items():
        report.append(f'- {k}: {v}')
    report.append('')
    report.append('## Issue fields')
    report.append('')
    for field in FIELDS[1:]:
        report.append(f'### {field}')
        for k,v in summary['field_counts'][field].items():
            report.append(f'- {k}: {v}')
        report.append('')
    (out/'human_quality_audit_report.md').write_text('\n'.join(report), encoding='utf-8')
    print(out/'human_quality_audit_report.md')

if __name__ == '__main__':
    main()
