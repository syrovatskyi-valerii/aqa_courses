
from lesson_28.UI.pages.base_page import BasePage
from lesson_28.UI.locators.home_page_locators import HomePageLocators



class HomePage(BasePage):


    def __init__(self, driver, url="https://guest:welcome2qauto@qauto2.forstudy.space/"):
        super().__init__(driver, url)



    def click_sign_in_button(self):

        self.click(
            locator=HomePageLocators.sign_in_button_loc,
            timeout=15,
            message='Cant find/click "Sign in" button on "Home Page"'
        )

        return self


    def click_registration_button(self):

        self.click(
            locator=HomePageLocators.registration_button,
            timeout=10,
            message='Cant find/click "Registration" button in "Log in" modal window'
        )

        return self


    def fill_in_name_field_like(self, name):

        self.fill_in_field(
            locator=HomePageLocators.name_field_loc,
            text=name,
            timeout=10,
            message='Cant fill in "Name" field in "Log in" modal window'
        )

        return self


    def fill_in_last_name_field_like(self, last_name):

        self.fill_in_field(
            locator=HomePageLocators.last_name_field_loc,
            text=last_name,
            timeout=10,
            message='Cant fill in "Last_name" field in "Log in" modal window'
        )

        return self


    def fill_in_email_field_like(self, email):

        self.fill_in_field(
            locator=HomePageLocators.email_field_loc,
            text=email,
            timeout=10,
            message='Cant fill in "Email" field in "Log in" modal window'
        )

        return self

    def fill_in_password_field_like(self, password):

        self.fill_in_field(
            locator=HomePageLocators.password_field_loc,
            text=password,
            timeout=10,
            message='Cant fill in "Password" field in "Log in" modal window'
        )

        return self


    def fill_in_re_enter_password_field_like(self, confirm_password):

        self.fill_in_field(
            locator=HomePageLocators.re_enter_password_field_loc,
            text=confirm_password,
            timeout=10,
            message='Cant fill in "Re-enter password" field in "Log in" modal window'
        )

        return self


    def click_on_register_submit_button(self):

        self.click(
            locator=HomePageLocators.register_submit_button,
            timeout=10,
            message='Cant find/click "Register" button in "Registration" modal window'
        )

        return self


    def fill_registration_form_valid_user_credentials(self, valid_user_credentials):

        return self.fill_in_name_field_like(valid_user_credentials["name"]) \
                    .fill_in_last_name_field_like(valid_user_credentials["last_name"]) \
                    .fill_in_email_field_like(valid_user_credentials["email"]) \
                    .fill_in_password_field_like(valid_user_credentials["password"]) \
                    .fill_in_re_enter_password_field_like(valid_user_credentials["password"])


    def fill_registration_form_invalid_user_credentials(self, invalid_user_credentials):

        self.fill_in_name_field_like(invalid_user_credentials["name"]) \
                    .fill_in_last_name_field_like(invalid_user_credentials["last_name"]) \
                    .fill_in_email_field_like(invalid_user_credentials["email"]) \
                    .fill_in_password_field_like(invalid_user_credentials["password"]) \
                    .fill_in_re_enter_password_field_like(invalid_user_credentials["password"])

        self.find(locator=HomePageLocators.registration_modal_window_loc).click()

        return self



    def verify_alert_user_already_exist(self):

        self.check_element_by_text(
            locator=HomePageLocators.alert_user_already_exists_loc,
            expected_text="User already exists",
            timeout=10
        )

        return self


    def click_on_all_inputs_in_registration_form(self):

        self.find(locator=HomePageLocators.name_field_loc).click()
        self.find(locator=HomePageLocators.last_name_field_loc).click()
        self.find(locator=HomePageLocators.email_field_loc).click()
        self.find(locator=HomePageLocators.password_field_loc).click()
        self.find(locator=HomePageLocators.re_enter_password_field_loc).click()
        self.find(locator=HomePageLocators.registration_modal_window_loc).click()

        return self


    def verify_that_inputs_is_required_in_registration_form(self):

        quantity_of_required_inputs = 5

        self.wait_several_elements(locator=HomePageLocators.validation_content_in_registration_form,
                                   quantity_of_els=quantity_of_required_inputs,
                                   timeout=10,
                                   message=f"Cant find all ({quantity_of_required_inputs}) required inputs "
                                           f"in Registration form"
                                   )
        return self


    def verify_that_inputs_return_validation_messages_in_registration_form(self):

        quantity_of_validation_messages = 5

        self.wait_several_elements(locator=HomePageLocators.invalid_validation_data_inputs,
                                   quantity_of_els=quantity_of_validation_messages,
                                   timeout=10,
                                   message=f"Cant find all ({quantity_of_validation_messages}) validation messages "
                                           f"in Registration form"
                                   )

        return self
