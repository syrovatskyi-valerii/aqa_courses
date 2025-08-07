from selenium.webdriver.common.by import By

class GaragePageLocators:

    registration_success_alert = (By.XPATH, "//div[@class='alert alert-success']/p[text()='Registration complete']")
    garage_header_loc = (By.XPATH, "//div/app-garage/div/div[1]/h1")

