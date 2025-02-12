# 🚀 Test Automation Framework using Playwright & Pytest

## 📌 Overview

This is an end-to-end (E2E) test automation framework built using **Python**, **Playwright**, and **Pytest**. It
supports **parallel execution** using `pytest-xdist` and dynamically generates test users via API.

---

## 🛠 Tech Stack

- **Python 3.12**
- **Playwright** (for UI Automation)
- **Pytest** (for test execution)
- **pytest-xdist** (for parallel execution)
- **pytest-check** (for soft assertions)
- **JSON** (for test data management)

---

## 📂 Project Structure

```
TestAutomationSite_e2e/
│── APIutils/
│   ├── create_user.py   # API utility to create test users
│── Pages/
│   ├── login.py         # Login page actions
│   ├── checkout.py      # Checkout page actions
│   ├── addProducts.py   # Add products to cart
│   ├── PlaceOrder.py    # Order confirmation handling
│── data/
│   ├── usercredentials.json  # User credentials for test execution
│── test_runner.py       # Main test execution file
│── conftest.py          # Fixture setup for browser and user management
│── README.md            # Project documentation
```

---

## 📥 Installation

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### **2️⃣ Create & Activate Virtual Environment**

```sh
python -m venv venv
# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### **3️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
playwright install
```

---

## 🚀 Running Tests

### **1️⃣ Run Tests Sequentially**

```sh
pytest FinalRun/test_runner.py -s
```

### **2️⃣ Run Tests in Parallel (Using `pytest-xdist`**)

```sh
pytest -n 4  # Run tests on 4 parallel workers
pytest -n auto  # Use all available CPU cores
```

### **3️⃣ Run Tests with HTML Report**

```sh
pytest --html=report.html --self-contained-html
```

---

## 🔄 Dynamic User Creation via API

Before tests start, users are **created dynamically via API** and then used for test execution.

- User details are stored in `data/usercredentials.json`
- Users are created via `create_user.py`
- If a user **already exists**, it is skipped

---

## 🛠 Troubleshooting

### **1️⃣ Locator Timeout Issue**

If elements take time to appear:

```python
self.page.wait_for_selector("#place-order-button", timeout=60000)
```

### **2️⃣ Test Failed Due to "User Already Exists"

Modify `create_user.py` to handle this gracefully:

```python
if response.status == 400 and "user_exists" in response.json().get("code", ""):
    print("User already exists, skipping creation.")
```

### **3️⃣ Browser Not Closing After Each Test**

Ensure browser fixture is correctly closing in `conftest.py`:

```python
yield browser_instance
browser_instance.browser.close()
```

---

## 📌 Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Added new feature"`
4. Push to GitHub: `git push origin feature-name`
5. Open a Pull Request 🚀

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📧 Contact

For any questions, reach out at [**suniljeurkar@gmail.com**](suniljeurkar@gmail.com) or create an issue on GitHub.

---

## ⚠️ Disclaimer

This website (`https://testautomationsite.in/`) has been hosted solely by me for demonstrating coding skills and
automation testing capabilities. It is intended for testing purposes only and may not be available in the future. Any
changes, interruptions, or unavailability of the site should be expected. The author holds no responsibility for any
external dependencies or third-party services linked to this project.

---

🚀 Happy Testing! 🎯

