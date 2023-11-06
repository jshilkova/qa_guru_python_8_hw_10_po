import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )

@pytest.fixture(scope="function", autouse=True)
def browser_setup(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }

    load_dotenv()
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    attach.add_logs(browser)

    browser.quit()
