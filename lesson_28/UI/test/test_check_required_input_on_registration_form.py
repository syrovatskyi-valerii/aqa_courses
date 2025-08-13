import pytest
import allure
from lesson_28.UI.test.conftest import BaseTest


@allure.feature('Validation required fields registration form')
@pytest.mark.user_registration_form
class TestRequiredFieldsRegistrationForm(BaseTest):

    @allure.severity(allure.severity_level.MINOR)
    @allure.story('Check required field in registration form')
    def test_check_required_input_on_registration_form(self, driver, home_page):

        """Verify that all mandatory fields in the registration form are marked as required
        and show validation messages when left empty."""

        home_page.open_page() \
            .click_sign_in_button() \
            .click_registration_button() \
            .click_on_all_inputs_in_registration_form() \
            .verify_that_inputs_is_required_in_registration_form()
