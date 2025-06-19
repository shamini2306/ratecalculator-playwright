# POS Malaysia Shipment Calculator Test Automation (Python)

This project contains automated tests for the POS Malaysia Shipment Calculator using Playwright and pytest-bdd.

## Features

- BDD-style test scenarios with Gherkin
- Page Object Model (POM) design pattern
- HTML test reports with screenshots

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup

1. Clone the repository
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install Playwright browsers:
   ```bash
   sudo python -m playwright install
   (or)
   playwright install
   ```

## Running Tests

To run tests with a browser UI:
```bash
python -m pytest tests/step_definition/test_shipment_steps.py  -vvs -m test --browser=chromium --headed --html=reports/report.html
```
## Test Case

### Verify user can calculate the shipment quote from Malaysia to India

1. Navigates to https://pos.com.my/send/ratecalculator
2. Enters "Malaysia" as "From" country
3. Enters "35600" as the postcode
4. Enters "India" as "To" country (leaving postcode empty)
5. Enters "1" as the weight
6. Clicks Calculate
7. Verifies multiple quotes are displayed

## Project Structure

- `tests/` - Contains test files
  - `features/` - Gherkin feature files
  - `step_definition/` test_shipment_steps.py` - Step implementations
  - `pages/` - Page object models
    - `shipment_calculator_page.py` - Page object for the shipment calculator
- `requirements.txt` - Project dependencies
- `pytest.ini` - Pytest configuration

## Dependencies

- Python 3.8+
- Playwright for Python
- Pytest
- Pytest-playwright
