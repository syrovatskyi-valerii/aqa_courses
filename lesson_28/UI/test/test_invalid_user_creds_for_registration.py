import pytest
import allure
from lesson_28.UI.test.conftest import BaseTest


@allure.feature('Validation invalid user creds')
@pytest.mark.user_registration_form
class TestInvalidUserCredsRegistrationData(BaseTest):

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Registration a user with invalid creds')
    def test_invalid_user_creds_for_registration(self, driver, home_page, invalid_user_credentials):

        """Verify that a user cannot register using invalid credentials and
        appropriate validation error messages are displayed in the registration form."""

        home_page.open_page() \
            .click_sign_in_button() \
            .click_registration_button() \
            .fill_registration_form_invalid_user_credentials(invalid_user_credentials) \
            .verify_that_inputs_return_validation_messages_in_registration_form()
