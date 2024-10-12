from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from urls import MAIN_URL, LOGIN_URL, PROFILE_URL, FORGOT_URL

def test_registered_user_navigates_to_main_page_via_header_logo(driver, create_user):
    unique_email, password = create_user

    driver.get(LOGIN_URL)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(PageLocators.EMAIL_FIELD)).send_keys(unique_email)
    driver.find_element(*PageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*PageLocators.SUBMIT_BUTTON).click()

    WebDriverWait(driver, 20).until(EC.url_to_be(MAIN_URL))
    assert driver.current_url == MAIN_URL

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 20).until(EC.url_to_be(PROFILE_URL))
    assert driver.current_url == PROFILE_URL

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(PageLocators.HEADER_LOGO)).click()
    WebDriverWait(driver, 20).until(EC.url_to_be(MAIN_URL))
    assert driver.current_url == MAIN_URL

    driver.get(FORGOT_URL)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(PageLocators.HEADER_LOGO)).click()
    WebDriverWait(driver, 20).until(EC.url_to_be(MAIN_URL))
    assert driver.current_url == MAIN_URL
