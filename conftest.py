import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument("Chrome")
    options.add_argument("--start-maximized")
    options.add_argument('--windows-size=1650,900')
    return options


@pytest.fixture
def web_driver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver

