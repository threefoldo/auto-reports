# ASHA EdFind Undergraduate Programs Extraction

This directory contains scripts and data for extracting undergraduate degree programs from the ASHA (American Speech-Language-Hearing Association) EdFind database.

## Source

**URL**: https://find.asha.org/ed/#sort=%40orderingid%20ascending&numberOfResults=100&f:@degreeprogram=[Undergraduate%20Degree]

## Extracted Data

### Files

- **asha_undergraduate_programs.json** - Complete program data in JSON format (292 programs)
- **asha_undergraduate_programs.csv** - Program data in CSV format for easy viewing in spreadsheet applications
- **extract_asha_coveo.py** - Main extraction script using Coveo API (recommended)
- **extract_asha_programs.py** - Alternative Selenium-based script (requires Chrome/Chromium)
- **extract_asha_api.py** - Analysis script used to discover the API configuration

### Data Fields

Each program entry contains:

- **title** - Institution name and degree type (e.g., "Alabama A&M University: Bachelor of Science (BS)")
- **uri/clickUri** - Direct link to the program details page
- **degree_program** - Always "Undergraduate Degree" for this dataset
- **location** - City and state (e.g., "Normal, Alabama")
- **city** - City name
- **state** - State name(s)
- **zip** - ZIP code
- **combined_program** - Whether it's a combined program
- **phone** - Contact phone number (if available)
- **email** - Contact email (if available)
- **website** - Program website (if available)
- **distance_learning** - Distance learning availability
- **accreditation** - Accreditation status
- **excerpt** - Description snippet from the program page

## Extraction Method

The ASHA EdFind page uses the **Coveo search platform** to dynamically load program listings. The extraction was accomplished by:

1. Analyzing the page source to identify the Coveo search infrastructure
2. Extracting the Coveo API configuration:
   - Organization ID: `americanspeechlanguagehearingassociationproductionh0xeoc4i`
   - Search endpoint: `https://[org-id].org.coveo.com/rest/search`
   - Authentication token (embedded in page)
3. Querying the Coveo REST API directly with the filter: `@degreeprogram=("Undergraduate Degree")`
4. Paginating through all results (100 results per page, 292 total programs)

## Running the Extraction

### Method 1: Direct API Query (Recommended)

```bash
python3 extract_asha_coveo.py
```

**Requirements**: `requests` library only
- Fast and reliable
- No browser required
- Directly queries the Coveo API

### Method 2: Browser Automation (Alternative)

```bash
pip3 install -r requirements_asha.txt
python3 extract_asha_programs.py
```

**Requirements**: Selenium, Chrome/Chromium browser
- Uses headless browser to render JavaScript
- More resource-intensive
- Useful if API configuration changes

## Statistics

- **Total Programs**: 292 undergraduate degree programs
- **Data Size**:
  - JSON: ~266 KB
  - CSV: ~175 KB
- **Extraction Date**: November 6, 2025
- **Filter Applied**: Undergraduate Degree programs only

## Sample Programs

1. Alabama A&M University: Bachelor of Science (BS) - Normal, Alabama
2. Appalachian State University: Bachelor of Science (BS) - Boone, North Carolina
3. Arkansas State University: Bachelor of Science (BS) - State University, Arkansas
4. Butler University: Bachelor of Arts (BA) - Indianapolis, Indiana
5. California State University, Chico: Bachelor of Science (BS) - Chico, California

## Notes

- The ASHA EdFind database contains over 300 institutions total across all program types (undergraduate, graduate, doctoral)
- This extraction focuses specifically on undergraduate degree programs
- Undergraduate programs are "Not Eligible for Accreditation" according to ASHA's accreditation guidelines
- The data includes programs in speech-language pathology, audiology, and speech, language, and hearing science

## Contact

For questions about the ASHA EdFind database, contact: AcademicAffairs@asha.org

## License

This is publicly available educational data from ASHA. Please respect ASHA's terms of use when using this data.
