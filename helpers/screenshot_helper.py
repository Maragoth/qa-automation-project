import os
from datetime import datetime


def take_screenshot(driver, name="screenshot", folder="screenshots"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path_folder = os.path.join(folder)
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)
    path = os.path.join(path_folder, f"{name}_{timestamp}.png")
    driver.save_screenshot(path)
    print(f"📸 Screenshot saved: {path}")
    return path
