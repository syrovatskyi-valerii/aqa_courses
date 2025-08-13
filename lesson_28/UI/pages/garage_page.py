from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

from lesson_28.UI.locators.garage_page_locators import GaragePageLocators
from lesson_28.UI.pages.base_page import BasePage


class GaragePage(BasePage):


    def __init__(self, driver, url='https://guest:welcome2qauto@qauto2.forstudy.space/'):
        super().__init__(driver, url)


    def check_that_user_located_on_garage_page(self):

        with allure.step("Check that user located on Garage page"):

            assert self._driver.current_url == self.url, \
                f"Current URL must be {self.url}, but it is {self._driver.current_url}"


            self.check_element_by_text(
                locator=GaragePageLocators.garage_header_loc,
                expected_text="Garage",
                timeout=10
            )

        return self


    def check_success_registration_alert(self):

        with allure.step("Verify that success registration alert is displayed"):

            self.check_element_by_text(
                locator=GaragePageLocators.registration_success_alert,
                expected_text="Registration complete",
                timeout=10
            )

        return self

