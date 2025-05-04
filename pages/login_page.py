# pages/login_page.py

import allure
from helpers.element_actions import safe_click, safe_type


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = ("id", "user-name")
        self.password_input = ("id", "password")
        self.login_button = ("id", "login-button")

    @allure.step("Logging in as: {username}")
    def login(self, username, password):
        safe_type(self.driver, self.username_input, username)
        safe_type(self.driver, self.password_input, password)
        safe_click(self.driver, self.login_button)
