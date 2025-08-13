from selenium.webdriver.common.by import By

class HomePageLocators:

    # Website header
    sign_in_button_loc = (By.XPATH, "//button[@class='btn btn-outline-white header_signin']")

    # Log in modal window
    registration_button = (By.XPATH, "//button[@class='btn btn-link' and text()='Registration']")

    # Registration modal window locators:
    registration_modal_window_loc = (By.XPATH,"//div[@class='modal-content']")
    name_field_loc = (By.CSS_SELECTOR, "#signupName")
    last_name_field_loc = (By.CSS_SELECTOR, "#signupLastName")
    email_field_loc = (By.CSS_SELECTOR, "#signupEmail")
    password_field_loc = (By.CSS_SELECTOR, "#signupPassword")
    re_enter_password_field_loc = (By.CSS_SELECTOR, "#signupRepeatPassword")
    register_submit_button = (By.XPATH, "//div/button[@class='btn btn-primary' and text()='Register']")
    validation_content_in_registration_form = (By.XPATH, "//div[@class='invalid-feedback']/p[contains(text(), 'required')]")
    invalid_validation_data_inputs = (By.XPATH, "//div[@class='invalid-feedback']")
    alert_user_already_exists_loc = (By.XPATH, "//p[@class='alert alert-danger' and text()='User already exists']")







