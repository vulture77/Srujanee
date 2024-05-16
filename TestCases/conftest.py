from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setUp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser=='firefox':
        driver = webdriver.Firefox()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#Hook for adding env info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Srujanee'
    config._metadata['Module Name'] = ''
    config._metadata['Tester Name'] = 'Siva'

#Hook for delete/modify env info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
