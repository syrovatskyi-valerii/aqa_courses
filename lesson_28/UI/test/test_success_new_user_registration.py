import pytest

@pytest.mark.positive
@pytest.mark.user_registration
def test_success_new_user_registration(driver, home_page, garage_page, valid_user_credentials):

    home_page.open_page() \
        .click_sign_in_button() \
        .click_registration_button() \
        .fill_registration_form_valid_user_credentials(valid_user_credentials) \
        .click_on_register_submit_button()

    garage_page.check_that_user_located_on_garage_page() \
        .check_success_registration_alert()
