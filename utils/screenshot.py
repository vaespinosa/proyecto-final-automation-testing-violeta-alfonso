import os
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), '../screenshots')
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

def take_screenshot(driver: WebDriver, test_name: str):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'{test_name}_{timestamp}.png'
    path = os.path.join(SCREENSHOT_DIR, filename)
    driver.save_screenshot(path)
    return path
