import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers.screenshot_helper import take_screenshot


@pytest.fixture
def setup():
    options = Options()

    # ✅ Use visual mode (headless disabled for now)
    options.add_argument("--headless=new")  # Use only if you're sure it's stable

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--guest")
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument(
        "--disable-features=AutofillServerCommunication,AutofillProfileServerData,PasswordManagerOnboarding,PasswordImport"
    )
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-extensions")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "autofill.profile_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
        },
    )

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("setup")
        if driver:
            test_name = item.name
            take_screenshot(driver, f"FAILED_{test_name}")
