from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from lesson_28.UI.test.custom_wait import WaitSeveralElements


class BasePage:

    def __init__(self, driver, url):
        self.url = url
        self._driver = driver


    def open_page(self):
        self._driver.get(self.url)

        return self


    def find(self, locator, timeout=5, message=None):
        element = WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(locator), message=message)

        return element


    def click(self, locator, timeout=5, message=None):
        element = WebDriverWait(self._driver, timeout).until(EC.element_to_be_clickable(locator),
               message=message)
        element.click()

        return element


    def fill_in_field(self, locator, text, timeout=5, clear_first=True, message =None):
        element = self.find(locator, timeout, message=message)
        if clear_first:
            element.clear()
        element.send_keys(text)

        return element


    def check_element_by_text(self, locator, expected_text, timeout=5, not_found_message=None, wrong_text_message=None):

        try:
            element = self.find(
                locator=locator,
                timeout=timeout,
                message=not_found_message or f"Element with locator {locator} not found"
            )

            assert expected_text in element.text, \
                wrong_text_message or f'Expected text "{expected_text}", but got: "{element.text}"'

        except TimeoutException:
            raise AssertionError(not_found_message or 'Timed out waiting for the expected element')

        return self


    def wait_several_elements(self, locator, quantity_of_els, timeout=5, message=None):
        element = WebDriverWait(self._driver, timeout
                           ).until(WaitSeveralElements(locator=locator, quantity=quantity_of_els),
                                   message=message)

        return element
