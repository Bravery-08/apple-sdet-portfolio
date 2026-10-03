import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from auto_maxim_devtools import maxim_devtools


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--auto-open-devtools-for-tabs')

    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(5)

    # maxim_devtools()

    yield drv
    drv.quit()
