from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from urls import MAIN_URL


def test_login_via_personal_account(driver, create_user):
    unique_email, password = create_user

    driver.get(MAIN_URL)

    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON)
    )
    personal_account_button.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PageLocators.EMAIL_FIELD)
    )
    password_input = driver.find_element(*PageLocators.PASSWORD_FIELD)
    login_button = driver.find_element(*PageLocators.SUBMIT_BUTTON)

    email_input.send_keys(unique_email)
    password_input.send_keys(password)

    login_button.click()

    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
    assert driver.current_url == MAIN_URL

    make_order_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PageLocators.MAKE_ORDER_BUTTON)
    )
    assert make_order_button.is_displayed()
