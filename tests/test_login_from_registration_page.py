from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from urls import REGISTER_URL, LOGIN_URL, MAIN_URL


def test_login_from_registration_page(driver, create_user):
    unique_email, password = create_user
    driver.get(REGISTER_URL)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PageLocators.ENTER_LOGIN_FORM)).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
    assert driver.current_url == LOGIN_URL

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(PageLocators.EMAIL_FIELD)).send_keys(unique_email)
    driver.find_element(*PageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*PageLocators.SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
    assert driver.current_url == MAIN_URL

    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(PageLocators.MAKE_ORDER_BUTTON)).is_displayed()
