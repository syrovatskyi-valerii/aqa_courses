import pytest
import allure
from lesson_28.UI.test.conftest import BaseTest


@allure.feature('User already exist')
@pytest.mark.user_registration_form
class TestUserAlreadyExist(BaseTest):

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Try to registration user which already exist')
    def test_registration_user_already_exist(self, driver, home_page, existing_user):

        """Verify registration is blocked for already existing user"""

        home_page.open_page() \
            .click_sign_in_button() \
            .click_registration_button() \
            .fill_registration_form_valid_user_credentials(existing_user) \
            .click_on_register_submit_button() \
            .verify_alert_user_already_exist()
