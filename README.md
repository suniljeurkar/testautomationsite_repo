# Test Automation Site E2E

## Overview

This project is an End-to-End (E2E) automation framework for testing an e-commerce website. It includes user
authentication, shopping, cart management, checkout, and order confirmation.

## Recent Updates

### **1. Using CSV for Product Selection**

- Products are now stored in `FinalRun/UIUtils/products.csv`.
- The test script reads this CSV and selects random products for each user.

### **2. Random Product Selection for Each User**

- Instead of using hardcoded product lists, we now use `sample()` from `random` to pick **3 random products** from the
  CSV file.
- This ensures test variability and better coverage.
- Fixed issue where `random.sample()` caused an `AttributeError` by using:
  ```python
  from random import sample
  ```

### **3. Fixed Random Module Issue**

- Issue: `AttributeError: 'builtin_function_or_method' object has no attribute 'sample'`.
- Fix: Instead of importing the entire `random` module, we now use:
  ```python
  from random import sample
  ```
- This avoids conflicts if `random` is accidentally shadowed in the script.

## Project Structure

```
FinalRun/
├── Pages/
│   ├── login.py
│   ├── gotoShop.py
│   ├── addProductsinShop.py
│   ├── viewcart.py
│   ├── checkout.py
│   ├── PlaceOrder.py
│
├── UIUtils/
│   ├── browserUtils.py
│   ├── dataUtils.py
│   ├── products.csv  # New CSV file for products
│
├── test_runner.py
├── conftest.py
├── requirements.txt
```

## How to Run Tests

Ensure dependencies are installed:
```sh
pip install -r requirements.txt
```

Run tests using `pytest`:
```sh
pytest test_runner.py --capture=no
```

## Debugging Tips

- If you face `random.sample()` errors:
    - Ensure `from random import sample` is used instead of `import random`.
    - Restart PyCharm/Python to clear cached issues.
- If test data is missing:
    - Verify `products.csv` has at least 3 products.
- Use verbose mode to debug:
  ```sh
  pytest test_runner.py -v --capture=no
  ```

## Next Improvements

- **Dynamic product selection**: Randomly vary the number of products selected (`k`) instead of always 3.
- **Parallel execution**: Run tests in parallel using `pytest-xdist` to improve speed.
- **Better error handling**: Improve logging when reading CSV files.

---
🚀 Happy Testing! Let me know if you need further updates!

