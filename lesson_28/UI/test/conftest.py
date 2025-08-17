import pytest
import allure
from selenium import webdriver
from shutil import which
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from lesson_28.UI.pages.garage_page import GaragePage
from lesson_28.UI.pages.home_page import HomePage
from lesson_28.UI.test.random_for_tests import generate_random_email


@pytest.mark.ui_tests
@allure.epic("Hillel course UI-tests")
@allure.testcase(url="https://lms.ithillel.ua/groups/6798d97ebcb884d43b014c4d/homeworks/687f47a517357ae9fd2389f7",
                 name="home_work_28_1")
class BaseTest:
    pass


@pytest.fixture(scope="function")
def driver():
    with allure.step("Launch browser"):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")

        driver_path = which("chromedriver")
        driver = webdriver.Chrome(service=Service(driver_path), options=options)

        yield driver

        with allure.step("Close browser"):
            driver.quit()


@pytest.fixture
def home_page(driver):
    return HomePage(driver=driver)


@pytest.fixture
def garage_page(driver):
    return GaragePage(driver=driver)


@pytest.fixture(scope="module")
def valid_user_credentials():
    email = generate_random_email()
    return {
        "name": "Test",
        "last_name": "User",
        "email": email,
        "password": "Test12345678"
    }


@pytest.fixture(scope="module")
def invalid_user_credentials():
    invalid_data = "йй"
    return {
        "name": invalid_data,
        "last_name": invalid_data,
        "email": invalid_data,
        "password": invalid_data
    }


@pytest.fixture
def existing_user(driver, home_page, garage_page, valid_user_credentials):

    creds = valid_user_credentials

    home_page.open_page() \
        .click_sign_in_button() \
        .click_registration_button() \
        .fill_registration_form_valid_user_credentials(creds) \
        .click_on_register_submit_button()

    return creds
