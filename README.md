# 🧪 QA Automation Project – E2E Testing with Selenium & Allure

This project is a simulated freelance task for a QA Automation Engineer role.  
It covers full end-to-end testing of the [SauceDemo](https://www.saucedemo.com) e-commerce site using **Selenium + Pytest + Allure**.

---

## 🎯 Project Goals

- ✅ Automate all main user flows (login, add to cart, checkout, logout)
- ✅ Include positive and negative test cases
- ✅ Capture screenshots and steps in Allure reports
- ✅ Ensure 100% stability with helper-based architecture
- ✅ Follow Page Object Model structure for clean, scalable code

---

## 🧰 Tech Stack

| Tool / Library     | Usage                            |
|--------------------|----------------------------------|
| Python             | Main programming language        |
| Selenium           | Web automation                   |
| Pytest             | Test framework                   |
| Allure             | Professional test reporting      |
| Pytest-html        | Optional secondary report format |
| Page Object Model  | Scalable test structure          |

---

## 📁 Folder Structure

qa_automation_project/
│
├── tests/ # All test files (positive + negative)
├── pages/ # Page Object classes (LoginPage, CheckoutPage, etc.)
├── helpers/ # Common utilities (click, type, wait, logger)
├── screenshots/ # Screenshots for passed steps
├── screenshots_failed/ # Screenshots for failed test steps
├── allure-results/ # Allure raw data (ignored in repo)
├── requirements.txt # Python dependencies
├── .gitignore # Files to exclude from Git
└── README.md # You’re reading it


---

## 🚀 How to Run Tests

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/qa-ecommerce-automation.git
cd qa-ecommerce-automation
```

2. (Optional) Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on macOS/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run all tests and generate Allure results
```bash
pytest tests/ --alluredir=allure-results
```

5. Serve Allure report
```bash
C:\Allure\bin\allure.bat serve allure-results
```
6. View the generated report.

Below is an example of a successful Allure report (100% passed):
![Allure Report – 100% Passed](images/allure_report_100.png)


👤 About Me as QA
I am a QA Automation enthusiast with a strong understanding of Selenium, Pytest, and modern test architecture.
My goal is to build reliable, readable, and real-world test frameworks using industry best practices.
I'm now seeking freelance or remote work as a QA Engineer.

✅ Summary
This project demonstrates my ability to:

Build full-stack automated testing from scratch

Design test architecture using Page Object Model

Generate readable and professional test reports

Ensure full test stability and isolation

Think like a QA Engineer – not just write tests

📫 If you're a client, feel free to connect with me on LinkedIn or reach out via Upwork / Test.io profile!