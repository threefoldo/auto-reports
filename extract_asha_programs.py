#!/usr/bin/env python3
"""
Script to extract undergraduate programs from ASHA EdFind
URL: https://find.asha.org/ed/#sort=%40orderingid%20ascending&numberOfResults=100&f:@degreeprogram=[Undergraduate%20Degree]
"""

import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def setup_driver():
    """Setup Chrome driver with headless options"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def extract_programs(url):
    """Extract all program information from the ASHA EdFind page"""
    driver = setup_driver()
    programs = []

    try:
        print(f"Loading URL: {url}")
        driver.get(url)

        # Wait for results to load (adjust selector based on actual page structure)
        print("Waiting for results to load...")
        wait = WebDriverWait(driver, 20)

        # Try multiple possible selectors for results
        result_selectors = [
            ".CoveoResult",
            ".result-item",
            ".program-item",
            "[class*='result']",
            "[class*='program']"
        ]

        results_loaded = False
        results_container = None

        for selector in result_selectors:
            try:
                results_container = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                results_loaded = True
                print(f"Found results using selector: {selector}")
                break
            except TimeoutException:
                continue

        if not results_loaded:
            # Try to get page source for debugging
            print("Could not find results with standard selectors. Analyzing page...")
            page_source = driver.page_source

            # Save page source for inspection
            with open('asha_page_source.html', 'w', encoding='utf-8') as f:
                f.write(page_source)
            print("Page source saved to asha_page_source.html")

            # Try to find any results in the page
            all_elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'result') or contains(@class, 'program') or contains(@class, 'Result')]")
            print(f"Found {len(all_elements)} potential result elements")

        # Give extra time for JavaScript to fully render
        time.sleep(5)

        # Try to extract program information
        # This will need to be adjusted based on actual page structure
        result_elements = driver.find_elements(By.CSS_SELECTOR, ".CoveoResult, .result-item, .program-item")

        print(f"Found {len(result_elements)} program results")

        for idx, element in enumerate(result_elements):
            try:
                program = {
                    'index': idx + 1,
                    'institution': '',
                    'program_name': '',
                    'degree_type': 'Undergraduate Degree',
                    'location': '',
                    'city': '',
                    'state': '',
                    'url': '',
                    'raw_html': element.get_attribute('outerHTML')
                }

                # Try to extract institution name
                try:
                    institution_elem = element.find_element(By.CSS_SELECTOR, ".institution, .school-name, [class*='institution'], h3, h4")
                    program['institution'] = institution_elem.text.strip()
                except NoSuchElementException:
                    pass

                # Try to extract program name
                try:
                    program_elem = element.find_element(By.CSS_SELECTOR, ".program-name, .title, [class*='program'], h2, h3")
                    program['program_name'] = program_elem.text.strip()
                except NoSuchElementException:
                    pass

                # Try to extract location
                try:
                    location_elem = element.find_element(By.CSS_SELECTOR, ".location, .address, [class*='location']")
                    program['location'] = location_elem.text.strip()
                except NoSuchElementException:
                    pass

                # Try to extract URL
                try:
                    link_elem = element.find_element(By.CSS_SELECTOR, "a")
                    program['url'] = link_elem.get_attribute('href')
                except NoSuchElementException:
                    pass

                programs.append(program)
                print(f"Extracted program {idx + 1}: {program.get('institution', 'Unknown')}")

            except Exception as e:
                print(f"Error extracting program {idx + 1}: {e}")
                continue

        # If no programs found with standard approach, try alternative
        if len(programs) == 0:
            print("\nNo programs found with standard extraction. Trying alternative approach...")

            # Get all text content
            body = driver.find_element(By.TAG_NAME, "body")
            full_text = body.text

            # Save for manual inspection
            with open('asha_page_text.txt', 'w', encoding='utf-8') as f:
                f.write(full_text)
            print("Full page text saved to asha_page_text.txt")

            # Check if there's a "no results" message
            if "no results" in full_text.lower() or "0 results" in full_text.lower():
                print("Page indicates no results found")
            else:
                print("Page loaded but program extraction needs adjustment")

    except Exception as e:
        print(f"Error during extraction: {e}")
        import traceback
        traceback.print_exc()

    finally:
        driver.quit()

    return programs

def save_programs(programs, output_file='asha_undergraduate_programs.json'):
    """Save extracted programs to JSON file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(programs, f, indent=2, ensure_ascii=False)
    print(f"\nSaved {len(programs)} programs to {output_file}")

def main():
    url = "https://find.asha.org/ed/#sort=%40orderingid%20ascending&numberOfResults=100&f:@degreeprogram=[Undergraduate%20Degree]"

    print("ASHA EdFind Program Extractor")
    print("=" * 50)

    programs = extract_programs(url)

    if programs:
        save_programs(programs)

        # Also save as CSV for easier viewing
        import csv
        csv_file = 'asha_undergraduate_programs.csv'
        if programs:
            keys = programs[0].keys()
            # Exclude raw_html from CSV
            csv_keys = [k for k in keys if k != 'raw_html']

            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=csv_keys)
                writer.writeheader()
                for program in programs:
                    row = {k: v for k, v in program.items() if k != 'raw_html'}
                    writer.writerow(row)
            print(f"Saved {len(programs)} programs to {csv_file}")
    else:
        print("\nNo programs were extracted. Please check:")
        print("1. The page source file (asha_page_source.html)")
        print("2. The page text file (asha_page_text.txt)")
        print("3. Adjust the CSS selectors in the script based on actual page structure")

if __name__ == "__main__":
    main()
