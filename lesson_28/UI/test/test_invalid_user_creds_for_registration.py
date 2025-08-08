import pytest

@pytest.mark.negative
@pytest.mark.user_registration
def test_invalid_user_creds_for_registration(driver, home_page, invalid_user_credentials):

    home_page.open_page() \
        .click_sign_in_button() \
        .click_registration_button() \
        .fill_registration_form_invalid_user_credentials(invalid_user_credentials) \
        .verify_that_inputs_return_validation_messages_in_registration_form()
