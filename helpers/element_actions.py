# helpers/element_actions.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def safe_click(driver, locator, timeout=10):
    """Click on the element if it is clickable."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        driver.execute_script("arguments[0].click();", element)
        print(f"✅ Clicked element: {locator}")
    except TimeoutException:
        print(f"❌ Could not click on element: {locator}")


def safe_type(driver, locator, text, timeout=10):
    """Enter text into the field (scroll, click, clear, send_keys) with basic security."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(0.1)
        element.clear()
        time.sleep(0.1)
        element.send_keys(text)
        time.sleep(0.1)

        value = element.get_attribute("value").strip()

        if value == text:
            print(f"✅ '{text}' entered in field: {locator}")
        else:
            print(f"❌ Final value different from expected: '{value}' != '{text}'")
            driver.save_screenshot(f"screenshots/FAILED_type_{locator[1]}.png")

    except TimeoutException:
        print(f"❌ Could not find field: {locator}")
        driver.save_screenshot(f"screenshots/FAILED_type_{locator[1]}.png")


def safe_get_text(driver, locator, timeout=10):
    """Get the text of the element if it is visible."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        text = element.text
        print(f"✅ Element text: '{text}' from {locator}")
        return text
    except TimeoutException:
        print(f"❌ Could not get text from: {locator}")
        driver.save_screenshot(f"screenshots/FAILED_get_text_{locator[1]}.png")
        return None


def safe_wait_for_element(driver, locator, timeout=10):
    """Wait for an element to be present on the page and return True/False."""
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        print(f"✅ The element appeared: {locator}")
        return True
    except TimeoutException:
        print(f"❌ The element did not appear: {locator}")
        return False


def safe_is_visible(driver, locator, timeout=10):
    """Check if the element is visible on the page."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        print(f"✅ Visible element: {locator}")
        return True
    except TimeoutException:
        print(f"❌ Element not visible: {locator}")
        return False


def safe_navigate_to(driver, url):
    """Go to the indicated page."""
    driver.get(url)
    print(f"🌐 Navigation to {url}")


def safe_wait_for_url_to_contain(driver, partial_url, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.url_contains(partial_url))
        print(f"✅ URL contains: {partial_url}")
    except:
        print(f"❌ URL does not contain: {partial_url}")
        raise


def safe_fill_field_js(driver, locator, value):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))

    driver.execute_script("arguments[0].focus();", element)
    for char in value:
        driver.execute_script(
            """
            arguments[0].value += arguments[1];
            arguments[0].dispatchEvent(new InputEvent('input', { bubbles: true }));
            """,
            element,
            char,
        )
        time.sleep(0.05)  # Optional: slows down typing like a human

    driver.execute_script(
        """
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        arguments[0].blur();
    """,
        element,
    )


def safe_type_js(driver, locator, text, timeout=10):
    """Entering text using send_keys + JS triggers (for React/Angular)."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(0.1)
        element.clear()
        time.sleep(0.1)
        element.send_keys(text)
        time.sleep(0.2)

        # JS backup dla React
        driver.execute_script("arguments[0].blur();", element)
        driver.execute_script(
            "arguments[0].dispatchEvent(new Event('input', { bubbles: true }));",
            element,
        )
        driver.execute_script(
            "arguments[0].dispatchEvent(new Event('change', { bubbles: true }));",
            element,
        )

        value = element.get_attribute("value").strip()
        if value == text:
            print(f"✅ Hybrid entered '{text}' in field: {locator}")
        else:
            print(f"❌ Hybrid did NOT enter correctly: '{value}' != '{text}'")
    except Exception as e:
        print(f"❌ Error in safe_type_hybrid: {e}")


def wait_for_password_popup_to_disappear(driver, timeout=5):
    try:
        WebDriverWait(driver, timeout).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']"))
        )
    except:
        pass  # don't wait forever, if it doesn't go away - continue


def safe_fill_field_by_paste(driver, locator, value):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    driver.execute_script(
        """
        const input = arguments[0];
        const value = arguments[1];
        input.focus();
        const dataTransfer = new DataTransfer();
        dataTransfer.setData('text', value);
        const event = new ClipboardEvent('paste', {
            clipboardData: dataTransfer,
            bubbles: true
        });
        input.dispatchEvent(event);
        input.value = value;
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
        input.blur();
    """,
        element,
        value,
    )


def safe_fill_field_action(driver, locator, value):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    element.click()
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.click()
    actions.send_keys(value)
    actions.perform()
