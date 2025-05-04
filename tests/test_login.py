import pytest
from pages.login_page import LoginPage
from helpers.element_actions import safe_navigate_to, safe_wait_for_url_to_contain
from helpers.test_logger import safe_step, log_step


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login_successful(self, setup):
        driver = setup
        login_page = LoginPage(driver)

        # Step 1: Navigate to the login page
        safe_navigate_to(driver, "https://www.saucedemo.com/")

        # Step 2: Login and take a screenshot
        safe_step(
            driver,
            lambda: login_page.login("standard_user", "secret_sauce"),
            "login_successful",
        )

        # Step 3: Check if the URL has changed on inventory
        safe_wait_for_url_to_contain(driver, "inventory")
        assert "inventory" in driver.current_url, "❌ Login failed!"
        print("✅ Login completed successfully.")
