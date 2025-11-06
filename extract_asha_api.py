#!/usr/bin/env python3
"""
Script to extract undergraduate programs from ASHA EdFind using API approach
"""

import json
import requests
from urllib.parse import urlencode

def try_coveo_api():
    """Attempt to query Coveo search API used by ASHA EdFind"""

    # Coveo search endpoint (common pattern)
    # The actual endpoint and token would need to be extracted from the page
    base_url = "https://find.asha.org"

    # Try to fetch the main page and look for API configuration
    try:
        print("Fetching main page to find API configuration...")
        response = requests.get(
            "https://find.asha.org/ed/",
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        )

        # Save the HTML for inspection
        with open('asha_raw_page.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print("Saved raw HTML to asha_raw_page.html")

        # Look for Coveo configuration in the page
        if 'Coveo' in response.text:
            print("Page uses Coveo search platform")

            # Try to extract API endpoint and token
            # These are typically embedded in JavaScript
            import re

            # Look for common Coveo patterns
            patterns = [
                r'searchApiUrl["\']?\s*:\s*["\']([^"\']+)',
                r'restUri["\']?\s*:\s*["\']([^"\']+)',
                r'endpoint["\']?\s*:\s*["\']([^"\']+)',
            ]

            for pattern in patterns:
                matches = re.findall(pattern, response.text)
                if matches:
                    print(f"Found potential API endpoint: {matches[0]}")

            # Look for access token
            token_patterns = [
                r'accessToken["\']?\s*:\s*["\']([^"\']+)',
                r'token["\']?\s*:\s*["\']([^"\']+)',
            ]

            for pattern in token_patterns:
                matches = re.findall(pattern, response.text)
                if matches:
                    print(f"Found potential token: {matches[0][:20]}...")

        # Try to find filter values
        if 'Undergraduate' in response.text:
            print("Found 'Undergraduate' in page content")

        return response.text

    except Exception as e:
        print(f"Error fetching page: {e}")
        return None

def try_direct_query():
    """Try to make direct API query to Coveo"""

    # Common Coveo REST API endpoint pattern
    api_url = "https://platform.cloud.coveo.com/rest/search/v2"

    # This would need the actual organization ID and API key
    # which we'd extract from the page

    print("\nNote: Direct API access requires:")
    print("1. Coveo organization ID")
    print("2. Coveo search token")
    print("3. Proper query structure")
    print("\nThese need to be extracted from the ASHA page JavaScript")

def extract_programs_from_html(html_content):
    """Try to extract any program information from raw HTML"""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_content, 'html.parser')

    programs = []

    # Save prettified HTML for easier inspection
    with open('asha_pretty.html', 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    print("Saved prettified HTML to asha_pretty.html")

    # Look for common result containers
    result_containers = soup.find_all(class_=lambda x: x and ('result' in x.lower() or 'program' in x.lower()))

    print(f"\nFound {len(result_containers)} potential result containers")

    # Get all text for analysis
    all_text = soup.get_text(separator='\n', strip=True)
    with open('asha_extracted_text.txt', 'w', encoding='utf-8') as f:
        f.write(all_text)
    print("Saved extracted text to asha_extracted_text.txt")

    # Look for script tags that might contain data
    scripts = soup.find_all('script')
    print(f"Found {len(scripts)} script tags")

    for i, script in enumerate(scripts):
        if script.string and ('program' in script.string.lower() or 'result' in script.string.lower()):
            with open(f'asha_script_{i}.js', 'w', encoding='utf-8') as f:
                f.write(script.string)
            print(f"Saved potentially relevant script to asha_script_{i}.js")

    return programs

def main():
    print("ASHA EdFind API Program Extractor")
    print("=" * 50)

    # Try to get the page content
    html_content = try_coveo_api()

    if html_content:
        # Try to extract programs
        programs = extract_programs_from_html(html_content)

        print("\n" + "=" * 50)
        print("ANALYSIS COMPLETE")
        print("=" * 50)
        print("\nThe ASHA EdFind page uses client-side JavaScript to load results.")
        print("\nTo extract the programs, you have these options:")
        print("\n1. Manual approach:")
        print("   - Visit the URL in a browser")
        print("   - Open Developer Tools (F12)")
        print("   - Go to Network tab")
        print("   - Look for API calls (likely to Coveo)")
        print("   - Copy the API endpoint and parameters")
        print("\n2. Browser automation (requires Chrome/Chromium):")
        print("   - Install Chrome or Chromium")
        print("   - Run: python3 extract_asha_programs.py")
        print("\n3. Browser extension:")
        print("   - Use a web scraping extension like Web Scraper or Data Miner")
        print("\n4. Check the files created:")
        print("   - asha_raw_page.html - raw HTML source")
        print("   - asha_pretty.html - formatted HTML")
        print("   - asha_extracted_text.txt - extracted text")
        print("   - asha_script_*.js - JavaScript files that may contain API config")

    try_direct_query()

if __name__ == "__main__":
    # Install beautifulsoup4 if not available
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("Installing beautifulsoup4...")
        import subprocess
        subprocess.check_call(['pip3', 'install', '-q', 'beautifulsoup4'])
        from bs4 import BeautifulSoup

    main()
