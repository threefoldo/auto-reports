#!/usr/bin/env python3
"""
Extract town/city and state information from ASHA program detail pages
"""

import json
import requests
import re
import time
from bs4 import BeautifulSoup
from typing import Dict, Optional, Tuple
import sys

def extract_location_from_page(url: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Fetch a program detail page and extract town/city and state

    Args:
        url: URL of the program detail page

    Returns:
        Tuple of (city, state) if found, (None, None) otherwise
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        city = None
        state = None

        # Method 1: Look for specific field labels containing "City" or "Location"
        for label_text in ['City:', 'Town:', 'Location:', 'Address:']:
            label_elem = soup.find(string=re.compile(label_text, re.I))
            if label_elem:
                parent = label_elem.parent
                if parent:
                    # Try to find the next sibling or value
                    next_elem = parent.find_next_sibling()
                    if next_elem:
                        text = next_elem.get_text(strip=True)
                        if text and not any(skip in text.lower() for skip in [':', 'state', 'zip']):
                            city = text
                            break

        # Method 2: Look for "State:" label
        for label_text in ['State:', 'State/Province:']:
            label_elem = soup.find(string=re.compile(label_text, re.I))
            if label_elem:
                parent = label_elem.parent
                if parent:
                    next_elem = parent.find_next_sibling()
                    if next_elem:
                        text = next_elem.get_text(strip=True)
                        if text and text not in [':', '']:
                            state = text
                            break

        # Method 3: Look for table rows with data fields
        # ASHA often uses tables with field captions
        table_rows = soup.find_all('tr')
        for row in table_rows:
            caption = row.get('data-caption', '').lower()
            field = row.get('data-field', '').lower()

            if 'city' in caption or 'city' in field:
                text = row.get_text(strip=True)
                # Remove the caption/label part
                text = re.sub(r'^[^:]*:\s*', '', text)
                if text:
                    city = text

            if 'state' in caption or 'state' in field:
                text = row.get_text(strip=True)
                text = re.sub(r'^[^:]*:\s*', '', text)
                if text:
                    state = text

        # Method 4: Look for divs/spans with class names containing location info
        for elem in soup.find_all(['div', 'span', 'p']):
            class_name = ' '.join(elem.get('class', [])).lower()
            if 'city' in class_name or 'location' in class_name:
                text = elem.get_text(strip=True)
                if text and len(text) < 50:  # Reasonable length for a city name
                    if not city and 'state' not in text.lower():
                        city = text

        # Method 5: Parse location from page text
        # Look for patterns like "City, State" or "City: XXX State: YYY"
        page_text = soup.get_text()

        # Pattern: City: Some City
        city_match = re.search(r'City:\s*([^,\n]+?)(?:\s*State:|$)', page_text, re.I)
        if city_match and not city:
            city = city_match.group(1).strip()

        # Pattern: State: Some State
        state_match = re.search(r'State:\s*([^,\n]+?)(?:\s*Zip:|$)', page_text, re.I)
        if state_match and not state:
            state = state_match.group(1).strip()

        return city, state

    except requests.exceptions.Timeout:
        print(f"  ⏱ Timeout fetching: {url}")
        return None, None
    except requests.exceptions.RequestException as e:
        print(f"  ❌ Error fetching {url}: {e}")
        return None, None
    except Exception as e:
        print(f"  ❌ Unexpected error for {url}: {e}")
        return None, None

def main():
    print("=" * 80)
    print("ASHA Program Location Extractor")
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
        'city_found': 0,
        'state_found': 0,
        'already_has_location': 0,
        'no_data': 0,
        'errors': 0
    }

    # Process each program
    for i, program in enumerate(programs, 1):
        title = program.get('title', 'Unknown')
        url = program.get('clickUri', program.get('uri', ''))
        existing_location = program.get('location', '')

        # Progress indicator
        progress = f"[{i}/{stats['total']}]"

        # Check if we already have location from API
        if existing_location and ',' in existing_location:
            # Already has "City, State" format from API
            stats['already_has_location'] += 1
            print(f"{progress} ✓ Already has location: {title[:50]} - {existing_location}")

            # Still parse it to make sure we have clean city and state fields
            parts = existing_location.split(',')
            if len(parts) >= 2:
                if not program.get('city'):
                    program['city'] = parts[0].strip()
                if not program.get('state'):
                    program['state'] = parts[1].strip()
            continue

        print(f"{progress} Fetching: {title[:60]}...")

        if not url:
            print(f"  ⚠ No URL available")
            stats['no_data'] += 1
            continue

        # Extract location from page
        city, state = extract_location_from_page(url)

        if city or state:
            if city:
                program['city'] = city
                stats['city_found'] += 1
                print(f"  ✓ Found city: {city}")
            if state:
                program['state'] = state
                stats['state_found'] += 1
                print(f"  ✓ Found state: {state}")

            # Update location field with "City, State" format
            if city and state:
                program['location'] = f"{city}, {state}"
            elif city:
                program['location'] = city
            elif state:
                program['location'] = state
        else:
            stats['no_data'] += 1
            print(f"  ⚠ No location data found")

        # Rate limiting - be polite to the server
        time.sleep(0.5)

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

    # Print statistics
    print()
    print("=" * 80)
    print("EXTRACTION COMPLETE")
    print("=" * 80)
    print(f"Total programs:              {stats['total']}")
    print(f"Already had location:        {stats['already_has_location']}")
    print(f"New cities extracted:        {stats['city_found']}")
    print(f"New states extracted:        {stats['state_found']}")
    print(f"No location data found:      {stats['no_data']}")
    print()

    # Count programs with location now
    with_location = sum(1 for p in programs if p.get('location'))
    with_city = sum(1 for p in programs if p.get('city'))
    with_state = sum(1 for p in programs if p.get('state'))

    print(f"Programs with location:      {with_location} ({with_location/len(programs)*100:.1f}%)")
    print(f"Programs with city:          {with_city} ({with_city/len(programs)*100:.1f}%)")
    print(f"Programs with state:         {with_state} ({with_state/len(programs)*100:.1f}%)")
    print()

    # Show sample
    programs_with_loc = [p for p in programs if p.get('location')]
    if programs_with_loc:
        print("Sample programs with location:")
        print("-" * 80)
        for p in programs_with_loc[:10]:
            print(f"• {p['title'][:50]}")
            print(f"  Location: {p.get('location', 'N/A')}")
            print(f"  City: {p.get('city', 'N/A')}, State: {p.get('state', 'N/A')}")
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
