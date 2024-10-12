from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from urls import MAIN_URL, LOGIN_URL, PROFILE_URL


def test_personal_account_redirect_for_registered_user(driver, create_user):
    unique_email, password = create_user

    driver.get(LOGIN_URL)

    WebDriverWait(driver, 20).until(
        EC.url_to_be(LOGIN_URL)
    )

    email_input_login = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(PageLocators.EMAIL_FIELD)
    )
    password_input_login = driver.find_element(*PageLocators.PASSWORD_FIELD)
    login_button = driver.find_element(*PageLocators.SUBMIT_BUTTON)

    email_input_login.send_keys(unique_email)
    password_input_login.send_keys(password)
    login_button.click()

    WebDriverWait(driver, 20).until(
        EC.url_to_be(MAIN_URL)
    )
    assert driver.current_url == MAIN_URL

    personal_account_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON)
    )
    personal_account_button.click()

    WebDriverWait(driver, 20).until(
        EC.url_to_be(PROFILE_URL)
    )
    assert driver.current_url == PROFILE_URL
