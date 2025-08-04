
from lesson_27.UI.pages.base_page import BasePage
from lesson_27.UI.locators.check_package_page_locators import CheckPackagePageLocators
from lesson_27.UI.pages.status_result_page import StatusResultPage




class CheckPackagePage(BasePage):


    def __init__(self, driver, url="https://tracking.novaposhta.ua/#/uk"):
        super().__init__(driver, url)


    def set_number_package(self, number_package):

        number_package_input = self._input(locator=CheckPackagePageLocators.number_package_input_loc,
                                      timeout=10, message='Cant find "Номер посилки" input on "Check Page Page"')
        number_package_input.send_keys(number_package)
        return self


    def click_search_button(self):
        self._button_clickable(locator=CheckPackagePageLocators.search_button_loc,timeout=10,
                               message='Cant find/click "Пошук" button on "Check Package Page"').click()
        return self



    def search_by_package_number(self, number_package) -> StatusResultPage:
        self.set_number_package(number_package)
        self.click_search_button()

        return StatusResultPage(self._driver)