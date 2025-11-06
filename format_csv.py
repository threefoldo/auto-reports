#!/usr/bin/env python3
"""
Format the ASHA programs data into a clean CSV file
"""

import json
import csv

def format_field(value):
    """Format field values properly for CSV"""
    if value is None or value == "":
        return ""
    if isinstance(value, list):
        # Join list items with semicolons
        return "; ".join(str(v) for v in value if v)
    return str(value)

def main():
    # Read the JSON data
    with open('asha_undergraduate_programs.json', 'r', encoding='utf-8') as f:
        programs = json.load(f)

    print(f"Loaded {len(programs)} programs")

    # Define the field order for CSV
    fieldnames = [
        'title',
        'location',
        'city',
        'state',
        'zip',
        'degree_program',
        'combined_program',
        'clickUri',
        'phone',
        'email',
        'website',
        'distance_learning',
        'accreditation',
        'excerpt'
    ]

    # Write to CSV with proper formatting
    with open('asha_undergraduate_programs.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        for program in programs:
            # Format each field properly
            row = {}
            for field in fieldnames:
                value = program.get(field, '')
                row[field] = format_field(value)

            writer.writerow(row)

    print(f"Wrote {len(programs)} programs to asha_undergraduate_programs.csv")

    # Print preview
    print("\nPreview of CSV (first 3 programs):")
    print("-" * 80)
    with open('asha_undergraduate_programs.csv', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i < 3:
                # Show truncated version for readability
                if len(line) > 200:
                    print(line[:200] + "...")
                else:
                    print(line.rstrip())
            else:
                break

if __name__ == "__main__":
    main()
