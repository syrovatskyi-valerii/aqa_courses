import pytest
import allure
from lesson_28.UI.test.conftest import BaseTest


@allure.feature('Create new user')
@pytest.mark.user_registration_form
class TestSuccessUserRegistration(BaseTest):

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('Registration a new user')
    def test_success_new_user_registration(self, driver, home_page, garage_page, valid_user_credentials):

        """Verify that a new user can register successfully and
        is redirected to the Garage page with a success alert."""

        home_page.open_page() \
            .click_sign_in_button() \
            .click_registration_button() \
            .fill_registration_form_valid_user_credentials(valid_user_credentials) \
            .click_on_register_submit_button()

        garage_page.check_that_user_located_on_garage_page() \
            .check_success_registration_alert()
