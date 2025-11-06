#!/usr/bin/env python3
"""
Extract email addresses from ASHA program detail pages
"""

import json
import csv
import requests
import re
import time
from bs4 import BeautifulSoup
from typing import Dict, Optional
import sys

def extract_email_from_page(url: str) -> Optional[str]:
    """
    Fetch a program detail page and extract email address

    Args:
        url: URL of the program detail page

    Returns:
        Email address if found, None otherwise
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Method 1: Look for mailto links
        mailto_links = soup.find_all('a', href=re.compile(r'^mailto:', re.I))
        if mailto_links:
            # Extract email from first mailto link
            mailto = mailto_links[0].get('href', '')
            email = mailto.replace('mailto:', '').split('?')[0].strip()
            if email:
                return email

        # Method 2: Search for email patterns in text
        # Common email regex pattern
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        # Get all text content
        text_content = soup.get_text()
        emails = re.findall(email_pattern, text_content)

        if emails:
            # Return the first valid email found
            # Filter out common false positives
            for email in emails:
                email = email.lower()
                # Skip example emails or obvious false positives
                if not any(skip in email for skip in ['example.com', 'domain.com', 'email.com', 'test@']):
                    return email

        # Method 3: Look for specific field labels
        # Look for elements near "Email:", "E-mail:", "Contact Email:", etc.
        for label in ['Email:', 'E-mail:', 'Contact Email:', 'Email Address:', 'E-Mail:']:
            label_elem = soup.find(string=re.compile(label, re.I))
            if label_elem:
                # Look for email in nearby text
                parent = label_elem.parent
                if parent:
                    parent_text = parent.get_text()
                    emails = re.findall(email_pattern, parent_text)
                    if emails:
                        return emails[0]

        return None

    except requests.exceptions.Timeout:
        print(f"  ⏱ Timeout fetching: {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"  ❌ Error fetching {url}: {e}")
        return None
    except Exception as e:
        print(f"  ❌ Unexpected error for {url}: {e}")
        return None

def main():
    print("=" * 80)
    print("ASHA Program Email Extractor")
    print("=" * 80)
    print()

    # Load existing data
    print("Loading program data...")
    with open('asha_undergraduate_programs.json', 'r', encoding='utf-8') as f:
        programs = json.load(f)

    print(f"Loaded {len(programs)} programs")
    print()

    # Track statistics
    stats = {
        'total': len(programs),
        'emails_found': 0,
        'emails_existing': 0,
        'no_email': 0,
        'errors': 0
    }

    # Process each program
    for i, program in enumerate(programs, 1):
        title = program.get('title', 'Unknown')
        url = program.get('clickUri', program.get('uri', ''))
        existing_email = program.get('email', '')

        # Progress indicator
        progress = f"[{i}/{stats['total']}]"

        # Skip if email already exists
        if existing_email and existing_email.strip():
            stats['emails_existing'] += 1
            print(f"{progress} ✓ Already has email: {title[:60]}")
            continue

        print(f"{progress} Fetching: {title[:60]}...")

        if not url:
            print(f"  ⚠ No URL available")
            stats['no_email'] += 1
            continue

        # Extract email from page
        email = extract_email_from_page(url)

        if email:
            program['email'] = email
            stats['emails_found'] += 1
            print(f"  ✓ Found email: {email}")
        else:
            stats['no_email'] += 1
            print(f"  ⚠ No email found")

        # Rate limiting - be polite to the server
        time.sleep(0.5)  # Wait 0.5 seconds between requests

        # Save progress every 50 programs
        if i % 50 == 0:
            print()
            print(f"💾 Saving progress... ({i} programs processed)")
            with open('asha_undergraduate_programs.json', 'w', encoding='utf-8') as f:
                json.dump(programs, f, indent=2, ensure_ascii=False)
            print()

    # Save final results
    print()
    print("=" * 80)
    print("Saving final results...")

    with open('asha_undergraduate_programs.json', 'w', encoding='utf-8') as f:
        json.dump(programs, f, indent=2, ensure_ascii=False)

    print("✓ Saved to asha_undergraduate_programs.json")

    # Also update CSV
    print("Updating CSV file...")
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

    print("✓ Saved to asha_undergraduate_programs.csv")

    # Print statistics
    print()
    print("=" * 80)
    print("EXTRACTION COMPLETE")
    print("=" * 80)
    print(f"Total programs:           {stats['total']}")
    print(f"Emails already present:   {stats['emails_existing']}")
    print(f"New emails extracted:     {stats['emails_found']}")
    print(f"No email found:           {stats['no_email']}")
    print(f"Total programs with email: {stats['emails_existing'] + stats['emails_found']}")
    print()

    # Show sample of programs with emails
    programs_with_email = [p for p in programs if p.get('email')]
    if programs_with_email:
        print("Sample programs with emails:")
        print("-" * 80)
        for p in programs_with_email[:10]:
            print(f"• {p['title'][:50]}")
            print(f"  Email: {p['email']}")
            print()

if __name__ == "__main__":
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("Installing beautifulsoup4...")
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'beautifulsoup4'])
        from bs4 import BeautifulSoup

    main()
