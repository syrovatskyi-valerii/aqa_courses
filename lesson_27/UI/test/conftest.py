import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from lesson_27.UI.pages.check_package_page import CheckPackagePage
from lesson_27.UI.pages.status_result_page import StatusResultPage


@pytest.fixture
def driver() -> webdriver:
    options = Options()
    options.add_argument("--headless")  # це додав в самому кінці, щоб спробувати, що працює без відкривання браузера
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def received_number_package():
    number_package = 20451198027178
    yield number_package

@pytest.fixture
def check_package_page(driver):
    return CheckPackagePage(driver=driver)

@pytest.fixture
def status_result_page(driver):
    return StatusResultPage(driver=driver)