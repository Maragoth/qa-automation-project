import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from helpers.element_actions import (
    safe_navigate_to,
    safe_wait_for_url_to_contain,
    wait_for_password_popup_to_disappear,
)
from helpers.test_logger import safe_step, log_step


@pytest.mark.usefixtures("setup")
class TestCheckoutProcess:

    def test_checkout_successful(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Step 1: Navigate to the Login Page
        safe_navigate_to(driver, "https://www.saucedemo.com/")

        # Step 2: Log in
        log_step("User Login")
        login_page.login("standard_user", "secret_sauce")

        # Step 3: Add product to cart
        log_step("Adding a product to the cart")
        product_page.add_product_to_cart("Sauce Labs Backpack")

        # Step 4: Go to your cart and start checkout
        cart_page.click_cart_icon()
        safe_wait_for_url_to_contain(driver, "cart.html")
        cart_page.click_checkout()

        # Step 5: Fill in your order details and take a screenshot
        safe_step(
            driver,
            lambda: (
                wait_for_password_popup_to_disappear(driver),
                checkout_page.fill_checkout_information("Jan", "Kowalski", "00-000"),
            ),
            "checkout_filled",
        )

        # Step 6: Click Continue and wait for the order summary
        checkout_page.click_continue_and_expect_step_two()
        checkout_page.wait_for_checkout_overview()

        # Step 7: Click Finish and take a screenshot of the success page
        safe_step(driver, lambda: checkout_page.click_finish(), "order_success")
        checkout_page.wait_for_success_message()

        # Step 8: Verify order success
        success_message = checkout_page.get_success_message()
        assert success_message is not None, "❌ No success message found!"
        assert (
            "THANK YOU FOR YOUR ORDER" in success_message.upper()
        ), "❌ The order was not completed correctly."
        print("✅ The order was completed successfully.")
