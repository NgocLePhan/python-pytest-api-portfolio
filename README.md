# 🚀 Python Pytest API Automation Testing Framework

[![API Automation Test Suite CI](https://github.com/NgocLePhan/python-pytest-api-portfolio/actions/workflows/api-tests.yml/badge.svg?branch=main)](https://github.com/NgocLePhan/python-pytest-api-portfolio/actions/workflows/api-tests.yml)
[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![Testing Framework](https://img.shields.io/badge/framework-pytest-orange.svg)](https://pytest.org/)

An enterprise-grade, scalable API Automation Testing Framework built with **Python**, **Pytest**, and **Requests**. This project demonstrates end-to-end API test automation practices including token authentication, data chaining (CRUD flows), data-driven testing (DDT), strict JSON Schema contract validation, and automated execution via GitHub Actions CI/CD pipeline.

---

## 🏗️ Framework Architecture & Features

* **Modular Test Design:** Clear separation of test suites, environment configs, schemas, and reports.
* **Dynamic Fixture Management:** Global fixtures in `conftest.py` providing session-level/function-level tokens, base URLs, and custom headers.
* **Data-Driven Testing (DDT):** Implemented using `@pytest.mark.parametrize` for boundary value and edge case coverage.
* **API Chaining (CRUD Lifecycle):** Automated data dependency flow (`POST` -> extract ID -> `PUT` update -> `DELETE`).
* **JSON Schema Validation:** Structural contract testing using `jsonschema` to catch backend contract regressions.
* **CI/CD Integration:** Automated test execution on Ubuntu cloud runners via GitHub Actions on every push/PR with downloadable HTML artifacts.
* **Rich Reporting:** Standalone HTML reporting using `pytest-html`.

---

## 📂 Project Structure

```text
python-pytest-api-portfolio/
│── .github/
│   └── workflows/
│       └── api-tests.yml         # GitHub Actions CI workflow
│── conftest.py                   # Pytest global fixtures & environment hooks
│── schemas.py                    # JSON Schema contract definitions
│── test_auth.py                  # Authentication & negative login test cases
│── test_products.py              # Catalog pagination & item detail tests
│── test_users_crud.py            # API chaining & CRUD lifecycle
│── test_users_ddt.py             # Data-driven test matrix
│── test_schema_validation.py     # Structural contract validation
│── requirements.txt              # Project dependencies
│── .env.example                  # Environment template
└── README.md                     # Project documentation
```

## ⚙️ Tech Stack & Libraries

| Tool / Library | Purpose |
| :--- | :--- |
| **Python 3.13** | Core programming language |
| **Pytest** | Test runner, assertions, and parameterized tests |
| **Requests** | HTTP client for RESTful API calls |
| **python-dotenv** | Environment variable management |
| **jsonschema** | JSON schema contract validation |
| **pytest-html** | Automated HTML test reporting |
| **GitHub Actions** | Continuous Integration (CI) execution |

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/NgocLePhan/python-pytest-api-portfolio.git](https://github.com/NgocLePhan/python-pytest-api-portfolio.git)
cd python-pytest-api-portfolio
```

### 2. Set up virtual environment & install dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```env
BASE_URL=[https://reqres.in](https://reqres.in)
API_PRIVATE_KEY=your_api_key_here
```

### 4. Execute test suites & generate HTML report

Run all test suites and produce a standalone HTML execution report:

```bash
python -m pytest -v -s --html=report.html --self-contained-html
```

## 📊 CI/CD Workflow

Every code change pushed or pull request submitted to the `main` branch automatically triggers the `.github/workflows/api-tests.yml` pipeline:

* **Automated Runner:** Sets up an isolated Ubuntu Linux environment with Python 3.13.
* **Secrets Ingestion:** Securely injects `API_PRIVATE_KEY` directly from GitHub Repository Secrets into the test runner.
* **Test Execution:** Executes the full Pytest test suite across all modules.
* **Artifact Archival:** Generates and uploads the standalone `report.html` as a downloadable build artifact for audit and review.
