from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # this will get value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):     # this will return browser value to setup method
    return request.config.getoption("--browser")

################# pytest HTML Report ################################################


# it is hook for Adding Enviroment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['tester'] = 'Mahendra Nikumbh'


# it is hook for delete/modify Enviroment info to HTML Report  # This hook we write bcz we does not want any infoemation on report so we remove from below statment
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)      # we dont want JAVA_HOME statment on report so we written none so JAVA_HOME not displayed on html report
    metadata.pop("Plugins", None)
