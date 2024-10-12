from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from urls import REGISTER_URL


def test_invalid_password(driver, generate_unique_email):
    driver.get(REGISTER_URL)

    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PageLocators.NAME_FIELD)
    )
    email_input = driver.find_element(*PageLocators.EMAIL_FIELD)
    password_input = driver.find_element(*PageLocators.PASSWORD_FIELD)
    register_button = driver.find_element(*PageLocators.SUBMIT_BUTTON)

    unique_email = generate_unique_email

    name_input.send_keys("Иван Иванов")
    email_input.send_keys(unique_email)
    password_input.send_keys("123")

    register_button.click()

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PageLocators.ERROR_MESSAGE)
    )

    assert error_message.is_displayed()

