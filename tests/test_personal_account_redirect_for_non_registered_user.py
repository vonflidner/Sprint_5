from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from urls import MAIN_URL, LOGIN_URL


def test_personal_account_redirect_for_non_registered_user(driver):
    driver.get(MAIN_URL)

    personal_account_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON)
    )
    personal_account_button.click()

    WebDriverWait(driver, 20).until(
        EC.url_to_be(LOGIN_URL)
    )
    assert driver.current_url == LOGIN_URL
