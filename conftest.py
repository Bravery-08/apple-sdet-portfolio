import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from auto_maxim_devtools import maxim_devtools


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def driver(request):
    # options = Options()
    # options.add_argument('--auto-open-devtools-for-tabs')

    browser = request.config.getoption("--browser")
    if browser == "firefox":
        drv = webdriver.Firefox()
    else:
        drv = webdriver.Chrome()

    drv.implicitly_wait(2)

    # maxim_devtools()

    yield drv
    drv.quit()
