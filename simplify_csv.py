#!/usr/bin/env python3
"""
Create a simplified CSV with only essential columns
"""

import json
import csv

def main():
    print("Creating simplified CSV with selected columns...")

    # Load the JSON data
    with open('asha_undergraduate_programs.json', 'r', encoding='utf-8') as f:
        programs = json.load(f)

    print(f"Loaded {len(programs)} programs")

    # Define only the columns we want to keep
    fieldnames = [
        'title',
        'email',
        'degree_program',
        'clickUri',
        'website'
    ]

    # Write to CSV with only selected columns
    with open('asha_undergraduate_programs.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        for program in programs:
            row = {}
            for field in fieldnames:
                value = program.get(field, '')
                if isinstance(value, list):
                    row[field] = "; ".join(str(v) for v in value if v)
                else:
                    row[field] = str(value) if value else ''
            writer.writerow(row)

    print(f"✓ Wrote {len(programs)} programs with {len(fieldnames)} columns")

    # Show preview
    print("\nPreview of simplified CSV:")
    print("-" * 80)
    with open('asha_undergraduate_programs.csv', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i < 6:
                print(line.rstrip())
            else:
                break

    # Show statistics
    with_email = sum(1 for p in programs if p.get('email'))
    with_website = sum(1 for p in programs if p.get('website'))

    print("\n" + "=" * 80)
    print("Statistics:")
    print(f"  Total programs: {len(programs)}")
    print(f"  Programs with email: {with_email} ({with_email/len(programs)*100:.1f}%)")
    print(f"  Programs with website: {with_website} ({with_website/len(programs)*100:.1f}%)")
    print("=" * 80)

if __name__ == "__main__":
    main()
