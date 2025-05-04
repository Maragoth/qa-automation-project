# pages/checkout_page.py

import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from helpers.element_actions import (
    safe_click,
    safe_get_text,
    safe_wait_for_element,
    safe_wait_for_url_to_contain,
)
from helpers.element_actions import safe_fill_field_action


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = ("id", "first-name")
        self.last_name_input = ("id", "last-name")
        self.postal_code_input = ("id", "postal-code")
        self.continue_button = ("id", "continue")
        self.finish_button = ("id", "finish")
        self.success_message = ("class name", "complete-header")
        self.summary_info = ("class name", "summary_info")
        self.error_message = ("xpath", "//h3[@data-test='error']")

    @allure.step("Filling checkout form: {first_name} {last_name}, ZIP: {postal_code}")
    def fill_checkout_information(self, first_name, last_name, postal_code):
        safe_fill_field_action(self.driver, self.first_name_input, first_name)
        safe_fill_field_action(self.driver, self.last_name_input, last_name)
        safe_fill_field_action(self.driver, self.postal_code_input, postal_code)

    @allure.step("Clicking Continue and expecting error")
    def click_continue_and_expect_error(self):
        safe_click(self.driver, self.continue_button)
        safe_wait_for_element(self.driver, self.error_message)

    @allure.step("Clicking Continue and waiting for step two screen")
    def click_continue_and_expect_step_two(self):
        # Save data before clicking (confirm that the fields are still filled in)
        fname = (
            self.driver.find_element(*self.first_name_input)
            .get_attribute("value")
            .strip()
        )
        lname = (
            self.driver.find_element(*self.last_name_input)
            .get_attribute("value")
            .strip()
        )
        zip_code = (
            self.driver.find_element(*self.postal_code_input)
            .get_attribute("value")
            .strip()
        )

        print(
            f"📋 Field values BEFORE click → First name: '{fname}', Last name: '{lname}', ZIP: '{zip_code}'"
        )
        if not (fname and lname and zip_code):
            self.driver.save_screenshot(
                "screenshots/FAILED_fields_before_click_continue.png"
            )
            raise AssertionError(
                "❌ One or more fields are empty before clicking Continue!"
            )

        # Click "Continue" and wait for the next screen
        safe_click(self.driver, self.continue_button)
        print("🕒 Clicked Continue, waiting for checkout-step-two.html...")

        # Wait for the URL to change
        safe_wait_for_url_to_contain(self.driver, "checkout-step-two.html", timeout=15)

    @allure.step("Clicking Finish")
    def click_finish(self):
        safe_wait_for_element(self.driver, self.finish_button)
        safe_click(self.driver, self.finish_button)

    @allure.step("Getting success message")
    def get_success_message(self):
        safe_wait_for_element(self.driver, self.success_message)
        return safe_get_text(self.driver, self.success_message)

    @allure.step("Waiting for checkout overview to load")
    def wait_for_checkout_overview(self):
        safe_wait_for_element(self.driver, self.summary_info)

    @allure.step("Waiting for success message to appear")
    def wait_for_success_message(self):
        safe_wait_for_element(self.driver, self.success_message)

    @allure.step("Reading error message if visible")
    def get_error_message(self):
        try:
            print(f"🕒 Waiting for error message: {self.error_message}")
            safe_wait_for_element(self.driver, self.error_message, timeout=3)
            text = safe_get_text(self.driver, self.error_message)
            print(f"✅ Error message read: {text}")
            return text
        except TimeoutException:
            print(
                f"❌ The error message did not appear for the selector: {self.error_message}"
            )
            return None
