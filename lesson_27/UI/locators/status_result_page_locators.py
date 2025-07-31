from selenium.webdriver.common.by import By

class StatusResultPageLocators:

    status_received_loc = (By.XPATH, "//*[@id='chat']/header/div[2]/div[2]/div[2]")
    ok_button_in_pop_up_loc = (By.CSS_SELECTOR, "button.button.v-btn.v-btn--depressed.v-btn--flat.v-btn--outlined.theme--light.v-size--default")