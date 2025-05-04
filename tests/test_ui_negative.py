import pytest
from pages.login_page import LoginPage
from helpers.test_logger import log_step
from helpers.element_actions import safe_navigate_to, safe_is_visible
from helpers.screenshot_helper import take_screenshot


@pytest.mark.usefixtures("setup")
class TestUINegative:

    def test_fake_elements_are_not_visible(self, setup):
        driver = setup
        login_page = LoginPage(driver)

        # Step 1: Navigate to the site and log in
        safe_navigate_to(driver, "https://www.saucedemo.com/")
        log_step("User Login")
        login_page.login("standard_user", "secret_sauce")

        # Step 2: Check that there is no invalid "buy_now_fake" button
        fake_button = ("id", "buy_now_fake")
        assert not safe_is_visible(driver, fake_button), "❌ Fake button found!"

        # Step 3: Check that there is no item with the text 'HACK MODE'
        hack_mode = ("xpath", "//*[contains(text(), 'HACK MODE')]")
        assert not safe_is_visible(
            driver, hack_mode
        ), "❌ Suspicious text 'HACK MODE' found!"

        # Step 4: Screenshot if everything is OK
        take_screenshot(driver, "ui_negative_elements_check")

        print("✅ No fake/unwanted UI elements found.")
