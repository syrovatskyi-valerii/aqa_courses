import pytest


@pytest.mark.negative
@pytest.mark.user_registration
def test_check_required_input_on_registration_form(driver, home_page):

    home_page.open_page() \
        .click_sign_in_button() \
        .click_registration_button() \
        .click_on_all_inputs_in_registration_form() \
        .verify_that_inputs_is_required_in_registration_form()
