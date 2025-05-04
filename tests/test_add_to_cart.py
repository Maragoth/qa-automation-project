import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from helpers.element_actions import (
    safe_navigate_to,
    safe_get_text,
    safe_wait_for_element,
)
from helpers.test_logger import safe_step, log_step


@pytest.mark.usefixtures("setup")
class TestAddToCart:

    def test_add_single_product_to_cart(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # Step 1: Go to the login page
        safe_navigate_to(driver, "https://www.saucedemo.com/")

        # Step 2: Log in
        login_page.login("standard_user", "secret_sauce")

        # Step 3: Add product to cart (take a screenshot)
        safe_step(
            driver,
            lambda: product_page.add_product_to_cart("Sauce Labs Backpack"),
            "product_added_to_cart",
        )

        # Step 4: Go to cart (take a screenshot)
        safe_step(driver, lambda: cart_page.click_cart_icon(), "cart_opened")

        # Step 5: Verify that the product is in your cart
        cart_item_locator = ("class name", "inventory_item_name")
        safe_wait_for_element(driver, cart_item_locator)
        cart_item_name = safe_get_text(driver, cart_item_locator)

        assert (
            "Sauce Labs Backpack" == cart_item_name
        ), f"❌ The Sauce Labs Backpack product was not successfully added to your cart!"
        print(
            f"✅ The Sauce Labs Backpack product has been successfully added to your cart."
        )
