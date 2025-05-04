import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from helpers.element_actions import safe_navigate_to
from helpers.test_logger import log_step
from helpers.screenshot_helper import take_screenshot


@pytest.mark.usefixtures("setup")
class TestUIElements:

    def test_product_page_ui_elements(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)

        # Step 1: Navigate to the login page
        safe_navigate_to(driver, "https://www.saucedemo.com/")

        # Step 2: Log in
        log_step("User Login")
        login_page.login("standard_user", "secret_sauce")

        # Step 3: Check the visibility of basic elements
        assert (
            product_page.is_product_title_visible()
        ), "❌ Product title is not visible."
        assert (
            product_page.is_product_sort_dropdown_visible()
        ), "❌ Sort dropdown is not visible."
        assert (
            product_page.is_first_product_name_visible()
        ), "❌ First product name is not visible."
        assert (
            product_page.is_first_product_price_visible()
        ), "❌ First product price is not visible."

        # Step 4: Screenshot if all elements are OK
        take_screenshot(driver, "ui_elements_visible")

        print("✅ All basic elements on the product page are visible.")
