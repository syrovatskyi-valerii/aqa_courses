import pytest

@pytest.mark.negative
@pytest.mark.user_registration
def test_registration_user_already_exist(driver, home_page, existing_user):

    home_page.open_page() \
        .click_sign_in_button() \
        .click_registration_button() \
        .fill_registration_form_valid_user_credentials(existing_user) \
        .click_on_register_submit_button() \
        .verify_alert_user_already_exist()
