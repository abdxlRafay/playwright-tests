# playwright-tests

Automated browser testing using Playwright and Python.

## Overview

A test automation suite built with **Playwright** and **Python** to validate real-world web application behaviour. The suite covers core user flows including page load verification, search functionality, and automated screenshot capture for visual evidence collection.

Built to demonstrate practical QA automation skills including test structure, assertion logic, and reproducible evidence capture.

## Features

- ✅ Page load validation — confirms pages respond and render correctly
- 🔍 Search functionality testing — automates input and verifies results
- 📸 Automated screenshot capture — saves visual evidence on test execution
- 🧪 Structured, readable test cases using Playwright's Python API

## Tech Stack

- Python 3.x
- Playwright (via `playwright` Python package)
- GitHub for version control and documentation

## Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/abdxlRafay/playwright-tests.git
cd playwright-tests
```

**2. Install dependencies**
```bash
pip install playwright
playwright install
```

**3. Run the tests**
```bash
python test_google.py
```

Screenshots will be saved automatically in the project directory upon execution.

## Project Structure

```
playwright-tests/
│
├── test_google.py       # Main test file — page load, search, screenshot
├── screenshot.png       # Auto-captured screenshot from latest test run
└── README.md
