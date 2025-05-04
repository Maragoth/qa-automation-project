import pytest
from pages.login_page import LoginPage
from helpers.test_logger import safe_step, log_step
from helpers.element_actions import safe_navigate_to


@pytest.mark.usefixtures("setup")
class TestLoginNegative:

    def test_login_with_invalid_credentials(self, setup):
        driver = setup
        login_page = LoginPage(driver)

        # Step 1: Navigate to the login page
        safe_navigate_to(driver, "https://www.saucedemo.com/")

        # Step 2: Try logging in with the wrong password
        safe_step(
            driver,
            lambda: login_page.login("standard_user", "wrong_password"),
            "login_attempt_invalid",
        )

        # Step 3: Check that we are still on the login page
        current_url = driver.current_url
        assert (
            "inventory" not in current_url
        ), "❌ Incorrect data, but user has been logged in!"
        print("✅ Attempting to log in with an incorrect password failed as expected.")
