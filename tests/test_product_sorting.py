import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from helpers.element_actions import safe_navigate_to
from helpers.test_logger import safe_step, log_step


@pytest.mark.usefixtures("setup")
class TestProductSorting:

    def test_product_sorting_all_methods(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)

        # Step 1: Navigate to the login page
        safe_navigate_to(driver, "https://www.saucedemo.com/")

        # Step 2: Log in
        log_step("User Login")
        login_page.login("standard_user", "secret_sauce")

        # 🔤 Sorting A-Z
        safe_step(
            driver, lambda: product_page.sort_products("az"), "products_sorted_az"
        )
        product_names_az = product_page.get_product_names()
        assert product_names_az == sorted(
            product_names_az
        ), "❌ A–Z: sorting doesn't work."
        print("✅ The products are sorted A–Z.")

        # 🔤 Sorting Z–A
        safe_step(
            driver, lambda: product_page.sort_products("za"), "products_sorted_za"
        )
        product_names_za = product_page.get_product_names()
        assert product_names_za == sorted(
            product_names_za, reverse=True
        ), "❌ Z–A: sorting doesn't work."
        print("✅ The products are sorted Z–A.")

        # 💲 Price: low to high
        safe_step(
            driver, lambda: product_page.sort_products("lohi"), "products_sorted_lohi"
        )
        product_prices_lohi = product_page.get_product_prices()
        assert product_prices_lohi == sorted(
            product_prices_lohi
        ), "❌ LO-HI: sorting doesn't work."
        print("✅ The products are sorted (ascending).")

        # 💲 Price: high to low
        safe_step(
            driver, lambda: product_page.sort_products("hilo"), "products_sorted_hilo"
        )
        product_prices_hilo = product_page.get_product_prices()
        assert product_prices_hilo == sorted(
            product_prices_hilo, reverse=True
        ), "❌ HI-LO: price sorting doesn't work."
        print("✅ Products are sorted by price (descending).")
