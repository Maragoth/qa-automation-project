import pytest
from pages.login_page import LoginPage
from pages.common_page import CommonPage
from helpers.test_logger import safe_step, log_step
from helpers.element_actions import safe_navigate_to, safe_wait_for_element


@pytest.mark.usefixtures("setup")
class TestLogout:

    def test_logout_successfully(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        common_page = CommonPage(driver)

        # Step 1: Navigate to the login page
        safe_navigate_to(driver, "https://www.saucedemo.com/")

        # Step 2: Log in
        log_step("User Login")
        login_page.login("standard_user", "secret_sauce")

        # Step 3: Make sure we are on the home page (inventory)
        assert (
            common_page.is_inventory_title_displayed()
        ), "❌ Inventory page title not visible."

        # Step 4: Open the menu
        common_page.open_menu()

        # Step 5: Click logout and take a screenshot
        safe_step(driver, lambda: common_page.click_logout(), "logout_successful")

        # Step 6: Wait for the login field with wait + screenshot
        login_field_locator = ("id", "user-name")
        safe_step(
            driver,
            lambda: safe_wait_for_element(driver, login_field_locator, timeout=10),
            "login_field_visible",
        )

        # Step 7: Verify that the login field has appeared
        assert safe_wait_for_element(
            driver, login_field_locator, timeout=5
        ), "❌ Login field did not appear after logging out."
        print("✅ Logout completed successfully.")
