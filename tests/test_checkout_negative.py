import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from helpers.test_logger import safe_step, log_step
from helpers.element_actions import safe_navigate_to, safe_wait_for_url_to_contain


@pytest.mark.usefixtures("setup")
class TestCheckoutNegative:

    def test_checkout_with_empty_fields(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        safe_navigate_to(driver, "https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

        log_step("Adding a product to the cart")
        product_page.add_product_to_cart("Sauce Labs Backpack")

        cart_page.click_cart_icon()
        cart_page.click_checkout()

        log_step("Sending a blank checkout form")
        checkout_page.fill_checkout_information("", "", "")

        safe_step(
            driver,
            lambda: checkout_page.click_continue_and_expect_error(),
            "checkout_continue_with_empty_fields",
        )

        error_msg = checkout_page.get_error_message()
        assert (
            error_msg is not None and "Error" in error_msg
        ), f"❌ No error message! Received: {error_msg}"
        print(f"✅ The error message appeared correctly: {error_msg}")
