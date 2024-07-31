from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=['chrome'], scope= "session", autouse=True)
def driver_init(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # elif request.param =='firefox':
    #     driver = webdriver.Firefox()
    request.driver = driver
    yield request.driver
    driver.close()

# def pytest_addoption(parser):
#     parser.addoption("--browser")

# @pytest.fixture(scope="session")
# def browser(request):
#     return request.config.getoption("--browser")

#Hook for adding env info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Srujanee'
    config._metadata['Module Name'] = ''
    config._metadata['Tester Name'] = 'Siva'

#Hook for delete/modify env info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Python", None)
