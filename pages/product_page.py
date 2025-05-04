# pages/product_page.py

import allure
from selenium.webdriver.support.ui import Select
from helpers.element_actions import safe_click, safe_wait_for_element, safe_is_visible


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.sort_dropdown = ("class name", "product_sort_container")
        self.product_names = ("class name", "inventory_item_name")
        self.product_title = ("class name", "title")  # "Products"
        self.product_prices = ("class name", "inventory_item_price")
        self.product_button = (
            "css selector",
            "button[data-test='add-to-cart-sauce-labs-backpack']",
        )

    @allure.step("Sorting products using method: {method_value}")
    def sort_products(self, method_value):
        """Sorts products by value (e.g. lohi, hilo)."""
        safe_wait_for_element(self.driver, self.sort_dropdown)
        sort_element = self.driver.find_element(*self.sort_dropdown)
        select = Select(sort_element)
        select.select_by_value(method_value)
        print(f"🔽 Products were sorted using the following method: {method_value}")

    @allure.step("Getting product names")
    def get_product_names(self):
        """Gets a list of product names."""
        safe_wait_for_element(self.driver, self.product_names)
        elements = self.driver.find_elements(*self.product_names)
        product_list = [el.text for el in elements]
        print(f"📦 Products on the website: {product_list}")
        return product_list

    @allure.step("Adding product to cart: {product_name}")
    def add_product_to_cart(self, product_name):
        # manually adjusted selector for a given product
        product_button = (
            "css selector",
            "button[data-test='add-to-cart-sauce-labs-backpack']",
        )

        safe_wait_for_element(self.driver, product_button)
        safe_click(self.driver, product_button)

    @allure.step("Checking if product title is visible")
    def is_product_title_visible(self):
        return safe_is_visible(self.driver, self.product_title)

    @allure.step("Checking if sort dropdown is visible")
    def is_product_sort_dropdown_visible(self):
        return safe_is_visible(self.driver, self.sort_dropdown)

    @allure.step("Checking if first product name is visible")
    def is_first_product_name_visible(self):
        return safe_is_visible(self.driver, self.product_names)

    @allure.step("Checking if first product price is visible")
    def is_first_product_price_visible(self):
        price_locator = ("class name", "inventory_item_price")
        return safe_is_visible(self.driver, price_locator)

    @allure.step("Getting product prices")
    def get_product_prices(self):
        """Gets a list of product prices as float."""
        locator = ("class name", "inventory_item_price")
        safe_wait_for_element(self.driver, locator)
        elements = self.driver.find_elements(locator[0], locator[1])
        prices = [float(el.text.replace("$", "")) for el in elements]
        print(f"💲 Product prices: {prices}")
        return prices
