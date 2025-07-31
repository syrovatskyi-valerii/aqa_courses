import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

MAIN_PAGE = 'http://localhost:8000/dz.html'
EXPECTED_ALERT_MSG = 'Верифікація пройшла успішно!'


FRAME_CONFIGS = [
    ("#frame1", "#input1", "Frame1_Secret", '//button[@onclick="verifyInput(\'input1\')"]'),
    ("#frame2", "#input2", "Frame2_Secret", '//button[@onclick="verifyInput(\'input2\')"]'),
]


@pytest.fixture(scope="module")
def driver():
    driver = Chrome()
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.mark.parametrize("frame_selector, input_selector, secret_message, check_button", FRAME_CONFIGS)
def test_verify_frame(driver, frame_selector, input_selector, secret_message, check_button):

    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, frame_selector))

    driver.find_element(By.CSS_SELECTOR, input_selector).send_keys(secret_message)

    driver.find_element(By.XPATH, check_button).click()

    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = Alert(driver)
        alert_text = alert.text

        assert alert_text == EXPECTED_ALERT_MSG, (
            f'Unexpected alert message: got "{alert_text}", expected "{EXPECTED_ALERT_MSG}"'
        )
        alert.accept()

    except TimeoutException:
        raise AssertionError('Alert did not appear after clicking the button')

    finally:
        driver.switch_to.default_content()
