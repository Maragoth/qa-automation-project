# helpers/test_logger.py

import os
import allure
from datetime import datetime
from helpers.screenshot_helper import take_screenshot


def log_step(step_description):
    print(f"📝 {step_description}")


def safe_step(driver, action_func, step_name="step"):
    """Performs action with log, screenshot and Allure step."""
    log_step(f"Starting the step: {step_name}")
    success = False
    screenshot_path = None

    with allure.step(step_name):
        try:
            result = action_func()
            # Success if no exception and function doesn't return False
            success = result if isinstance(result, bool) else True
        except Exception as e:
            print(f"❌ Exception in step '{step_name}': {e}")
            success = False

        # Always take screenshot (success or not)
        screenshot_path = take_screenshot(driver, step_name)

        if success:
            print(f"✅ Step completed: {step_name}")
        else:
            print(f"❌ Step FAILED: {step_name}")

        # Attach to Allure report
        if screenshot_path:
            allure.attach.file(
                screenshot_path,
                name=step_name,
                attachment_type=allure.attachment_type.PNG,
            )
