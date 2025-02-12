# 📌 Test Automation Site E2E - README

## 🚀 New Feature: CLI-Based Browser Selection

### 🎯 **Overview**

We have introduced a new **command-line interface (CLI) feature** that allows users to dynamically select the browser
for test execution. This feature enhances flexibility and enables testing across multiple browsers without modifying the
code.

---

## 🔹 **New CLI Argument: `--browser-name`**

| Browser Name (CLI Argument) | Playwright Equivalent |
|-----------------------------|-----------------------|
| `chromium`                  | Chromium (Default)    |
| `firefox`                   | Firefox               |
| `webkit`                    | Webkit (Safari)       |

### ✅ **Usage**

Run tests with a specific browser using the following command:

```sh
pytest .\FinalRun\test_runner.py --browser-name=firefox
```

Example for Chromium:

```sh
pytest .\FinalRun\test_runner.py --browser-name=chromium
```

---

## 🔧 **Implementation Details**

### 📌 **Changes in `conftest.py`**

- Added `pytest_addoption` to accept `--browser-name` as a CLI argument.
- Updated the `browser` fixture to dynamically launch the specified browser.

### 📌 **Changes in `browserUtils.py`**

- Modified `BrowserInstance` to accept the browser type and initialize it accordingly.
- Allowed "chrome" as an alias for "chromium" to enhance usability.

---

## 🛠 **Additional Fixes & Enhancements**

### ✅ **Improved API User Creation Handling**

- The framework now skips user creation if a user already exists, preventing redundant API calls and test failures.

### ✅ **Registered Pytest Marks (`smoke`, `regression`)**

- Added `pytest.ini` configurations to avoid warnings when using `@pytest.mark.smoke` and `@pytest.mark.regression`.

```ini
[pytest]
markers =
    smoke: Smoke tests
    regression: Regression tests
```

---

## 📜 **How to Run Tests**

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run tests with the desired browser:
   ```sh
   pytest .\FinalRun\test_runner.py --browser-name=chromium
   ```

---

## 📢 **Next Steps**

- Implement headless mode support for faster execution.
- Add logging and reporting for better debugging.
- Integrate with CI/CD pipelines for automated test execution.

---

🔹 *For any issues or contributions, feel free to raise a pull request or open an issue!* 🚀

