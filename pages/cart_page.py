# pages/cart_page.py

import allure
import time
from helpers.element_actions import safe_click, safe_wait_for_element
from helpers.element_actions import safe_wait_for_url_to_contain


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = ("class name", "shopping_cart_link")
        self.checkout_button = ("id", "checkout")
        self.cart_list = ("class name", "cart_list")

    @allure.step("Clicking cart icon")
    def click_cart_icon(self):
        safe_wait_for_element(self.driver, self.cart_icon)
        safe_click(self.driver, self.cart_icon)

    @allure.step("Clicking checkout button from cart page")
    def click_checkout(self):
        safe_wait_for_url_to_contain(self.driver, "cart.html", timeout=5)
        print("✅ We are on the shopping cart page")
        safe_wait_for_element(self.driver, self.cart_list)
        print("✅ Cart_list is visible")
        safe_wait_for_element(self.driver, self.checkout_button)
        print("✅ Checkout_button is visible")
        safe_click(self.driver, self.checkout_button)
        print("✅ Checkout_button is clicked")

    @allure.step("Clicking checkout button with retry (max_attempts={max_attempts})")
    def click_checkout_with_retry(self, max_attempts=3):
        """Click 'Checkout' if we are on the shopping cart page. Retry only if the URL does not change."""

        for attempt in range(1, max_attempts + 1):
            print(f"🔁 Attempting to click 'Checkout' (approach {attempt})")

            try:
                safe_wait_for_element(self.driver, self.checkout_button)
                safe_click(self.driver, self.checkout_button)
                print("✅ Clicked 'Checkout'")
            except Exception as e:
                print(f"❌ Error after clicking 'Checkout': {e}")

            if safe_wait_for_url_to_contain(
                self.driver, "checkout-step-one.html", timeout=5
            ):
                print("✅ Successfully completed transition to checkout form.")
                return
            else:
                print("❌ URL does not contain 'checkout-step-one.html' — retry...")

        raise AssertionError(
            "❌ Could not proceed to checkout form after multiple attempts."
        )
