# pages/common_page.py

import allure
from helpers.element_actions import safe_click, safe_wait_for_element


class CommonPage:

    def __init__(self, driver):
        self.driver = driver
        self.menu_button = ("id", "react-burger-menu-btn")
        self.logout_link = ("id", "logout_sidebar_link")
        self.inventory_title = (
            "class name",
            "title",
        )  # on the home page, e.g. "Products"

    @allure.step("Opening side menu")
    def open_menu(self):
        safe_wait_for_element(self.driver, self.menu_button)
        safe_click(self.driver, self.menu_button)

    @allure.step("Clicking logout")
    def click_logout(self):
        safe_wait_for_element(self.driver, self.logout_link)
        safe_click(self.driver, self.logout_link)

    @allure.step("Checking if inventory title is displayed")
    def is_inventory_title_displayed(self):
        return safe_wait_for_element(self.driver, self.inventory_title, timeout=5)

    @allure.step("Checking if logout button is visible")
    def is_logout_button_visible(self):
        return safe_wait_for_element(self.driver, self.logout_link, timeout=5)
