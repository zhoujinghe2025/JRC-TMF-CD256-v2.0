#!/usr/bin/env python3
"""Compare two independent human audit CSV files.

Usage:
  python scripts/compare_human_audits.py --reviewer1 docs/human_quality_audit_reviewer1.csv --reviewer2 docs/human_quality_audit_reviewer2.csv --out-dir quality_report/human_audit_comparison
"""
import argparse, csv, json
from collections import Counter
from pathlib import Path


def load(path):
    with open(path, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    return {r['audit_id']: r for r in rows}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--reviewer1', required=True)
    ap.add_argument('--reviewer2', required=True)
    ap.add_argument('--out-dir', required=True)
    args = ap.parse_args()
    r1 = load(args.reviewer1); r2 = load(args.reviewer2)
    ids = sorted(set(r1) | set(r2))
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    rows=[]; counts=Counter()
    for aid in ids:
        a=r1.get(aid,{}); b=r2.get(aid,{})
        s1=(a.get('audit_status') or '').strip(); s2=(b.get('audit_status') or '').strip()
        agree = bool(s1 and s2 and s1 == s2)
        if agree: counts['agree'] += 1
        else: counts['disagree_or_blank'] += 1
        rows.append({
            'audit_id': aid,
            'sample_id': a.get('sample_id') or b.get('sample_id') or '',
            'reviewer1_status': s1,
            'reviewer2_status': s2,
            'status_agreement': 'yes' if agree else 'no',
            'reviewer1_notes': a.get('notes',''),
            'reviewer2_notes': b.get('notes',''),
            'final_status': s1 if agree else '',
            'adjudicator': '',
            'adjudication_date': '',
            'final_notes': '',
        })
    fields=list(rows[0].keys()) if rows else []
    with (out/'human_audit_reviewer_comparison.csv').open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
    summary={'reviewer1': args.reviewer1, 'reviewer2': args.reviewer2, 'total': len(ids), 'counts': dict(counts), 'agreement_rate': counts['agree']/len(ids) if ids else None}
    (out/'human_audit_reviewer_comparison_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(out/'human_audit_reviewer_comparison.csv')

if __name__ == '__main__':
    main()
