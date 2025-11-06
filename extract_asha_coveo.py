#!/usr/bin/env python3
"""
Script to extract undergraduate programs from ASHA EdFind using Coveo API
Extracted configuration from: https://find.asha.org/ed/
"""

import json
import requests
import csv
from typing import List, Dict

# Coveo configuration extracted from the ASHA page
COVEO_ORG_ID = "americanspeechlanguagehearingassociationproductionh0xeoc4i"
COVEO_TOKEN = "xx2ab53281-e908-44ae-b622-adbd56de71c1"
COVEO_ENDPOINT = f"https://{COVEO_ORG_ID}.org.coveo.com/rest/search"

def query_coveo_api(
    query: str = "",
    filters: Dict = None,
    number_of_results: int = 100,
    first_result: int = 0
) -> Dict:
    """
    Query the Coveo API for ASHA programs

    Args:
        query: Search query string
        filters: Dictionary of field filters
        number_of_results: Number of results per page
        first_result: Offset for pagination

    Returns:
        Dictionary containing the API response
    """

    headers = {
        "Authorization": f"Bearer {COVEO_TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    # Build the request payload
    payload = {
        "q": query,
        "numberOfResults": number_of_results,
        "firstResult": first_result,
        "searchHub": "EdFind",
        "enableDidYouMean": True,
        "sortCriteria": "@orderingid ascending"
    }

    # Add filters if provided
    if filters:
        # Build advanced query with filters
        aq_parts = []
        for field, value in filters.items():
            if isinstance(value, list):
                # Multiple values - use OR
                values_str = " OR ".join([f'"{v}"' for v in value])
                aq_parts.append(f"@{field}=({values_str})")
            else:
                aq_parts.append(f'@{field}=="{value}"')

        if aq_parts:
            payload["aq"] = " AND ".join(aq_parts)

    try:
        print(f"Querying Coveo API (offset: {first_result}, limit: {number_of_results})...")
        if filters:
            print(f"Filters: {payload.get('aq', 'None')}")

        response = requests.post(
            COVEO_ENDPOINT,
            headers=headers,
            json=payload,
            timeout=30
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error querying Coveo API: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status: {e.response.status_code}")
            print(f"Response body: {e.response.text}")
        return None

def extract_program_data(result: Dict) -> Dict:
    """Extract relevant program information from a Coveo result"""

    raw = result.get('raw', {})

    program = {
        'title': result.get('title', ''),
        'uri': result.get('uri', ''),
        'clickUri': result.get('clickUri', ''),
        'degree_program': raw.get('degreeprogram', ''),
        'location': raw.get('location', ''),
        'combined_program': raw.get('combinedprogram', ''),
        'institution': raw.get('institution', ''),
        'city': raw.get('city', ''),
        'state': raw.get('state', ''),
        'zip': raw.get('zip', ''),
        'phone': raw.get('phone', ''),
        'email': raw.get('email', ''),
        'website': raw.get('website', ''),
        'distance_learning': raw.get('distancelearning', ''),
        'accreditation': raw.get('accreditation', ''),
        'excerpt': result.get('excerpt', ''),
    }

    return program

def get_all_programs(filters: Dict = None, max_results: int = 1000) -> List[Dict]:
    """
    Retrieve all programs matching the filters

    Args:
        filters: Dictionary of field filters
        max_results: Maximum number of results to retrieve

    Returns:
        List of program dictionaries
    """

    all_programs = []
    results_per_page = 100
    first_result = 0
    total_count = None

    while True:
        response = query_coveo_api(
            filters=filters,
            number_of_results=results_per_page,
            first_result=first_result
        )

        if not response:
            print("Failed to get response from API")
            break

        # Get total count on first request
        if total_count is None:
            total_count = response.get('totalCount', 0)
            print(f"Total programs found: {total_count}")

        # Extract results
        results = response.get('results', [])
        if not results:
            print("No more results")
            break

        # Process each result
        for result in results:
            program = extract_program_data(result)
            all_programs.append(program)

        print(f"Retrieved {len(all_programs)} / {total_count} programs")

        # Check if we've retrieved all results
        first_result += len(results)
        if first_result >= total_count or len(all_programs) >= max_results:
            break

        # Pagination - continue to next page
        if len(results) < results_per_page:
            break

    return all_programs

def save_programs_json(programs: List[Dict], filename: str = 'asha_undergraduate_programs.json'):
    """Save programs to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(programs, f, indent=2, ensure_ascii=False)
    print(f"\nSaved {len(programs)} programs to {filename}")

def save_programs_csv(programs: List[Dict], filename: str = 'asha_undergraduate_programs.csv'):
    """Save programs to CSV file"""
    if not programs:
        print("No programs to save")
        return

    # Get all unique keys
    all_keys = set()
    for program in programs:
        all_keys.update(program.keys())

    fieldnames = sorted(all_keys)

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(programs)

    print(f"Saved {len(programs)} programs to {filename}")

def main():
    print("=" * 70)
    print("ASHA EdFind Undergraduate Programs Extractor")
    print("Using Coveo API")
    print("=" * 70)
    print()

    # Filter for undergraduate degree programs
    filters = {
        "degreeprogram": ["Undergraduate Degree"]
    }

    # Get all programs
    programs = get_all_programs(filters=filters)

    if programs:
        print()
        print("=" * 70)
        print(f"Successfully extracted {len(programs)} undergraduate programs")
        print("=" * 70)

        # Save to both JSON and CSV
        save_programs_json(programs)
        save_programs_csv(programs)

        # Print sample of first few programs
        print("\nSample of extracted programs:")
        print("-" * 70)
        for i, program in enumerate(programs[:5], 1):
            print(f"\n{i}. {program.get('title', 'No title')}")
            print(f"   Location: {program.get('location', 'N/A')}")
            print(f"   Degree: {program.get('degree_program', 'N/A')}")
            print(f"   URL: {program.get('clickUri', 'N/A')}")

        if len(programs) > 5:
            print(f"\n... and {len(programs) - 5} more programs")
    else:
        print("\nNo programs were extracted. Please check the error messages above.")

if __name__ == "__main__":
    main()
