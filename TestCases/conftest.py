import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        serv_obj = Service("C:\Drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)

    elif browser == 'firefox':
        serv_obj = Service("C:\Drivers\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
    else:
        serv_obj = Service("C:\Drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)

    return driver


# For getting browser selection in command prompt
# This will get the value from CLI/Hooks
def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return the browser value to above setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

'''
# To generate pytest HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)
'''