from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from lesson_27.UI.locators.status_result_page_locators import StatusResultPageLocators
from lesson_27.UI.pages.base_page import BasePage

RECEIVED_STATUS = 'Отримана'


class StatusResultPage(BasePage):

    def __init__(self, driver, url='https://tracking.novaposhta.ua/#/uk/chat/messages'):
        super().__init__(driver, url)


    def click_on_ok_button_in_pop_up(self):
        self._button_clickable(locator=StatusResultPageLocators.ok_button_in_pop_up_loc, timeout=10,
                               message='Cant find/click "Добре" button in pop-up"').click()
        return self


    def check_received_status(self):
        assert self._driver.current_url == self.url, \
            f"Current URL must be {self.url}, but it is {self._driver.current_url}"

        try:
            element = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located(StatusResultPageLocators.status_received_loc),
                message='Cannot find element(status) - "Отримана" on status result page'
            )

            assert RECEIVED_STATUS in element.text, \
                f'Expected status "{RECEIVED_STATUS}", but got: "{element.text}"'

        except TimeoutException:
            raise AssertionError('Timed out waiting for status element on status result page')