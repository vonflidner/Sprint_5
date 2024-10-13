import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from urls import REGISTER_URL, MAIN_URL, LOGIN_URL
from faker import Faker
import random

fake = Faker()

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.fixture
def open_registration_page(driver):
    def _open():
        driver.get("https://stellarburgers.nomoreparties.site/register")
    return _open

@pytest.fixture
def generate_unique_email():
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    cohort_number = random.randint(1000, 9999)
    random_digits = random.randint(100, 999)
    domain = "yandex.ru"
    return f"{first_name}_{last_name}_{cohort_number}_{random_digits}@{domain}"

@pytest.fixture
def generate_password():
    return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

@pytest.fixture
def create_user(driver, generate_unique_email, generate_password):
    unique_email = generate_unique_email
    password = generate_password

    driver.get(REGISTER_URL)

    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(PageLocators.NAME_FIELD)
    )
    email_input = driver.find_element(*PageLocators.EMAIL_FIELD)
    password_input = driver.find_element(*PageLocators.PASSWORD_FIELD)
    register_button = driver.find_element(*PageLocators.SUBMIT_BUTTON)

    name_input.send_keys(f"{fake.first_name()} {fake.last_name()}")
    email_input.send_keys(unique_email)
    password_input.send_keys(password)
    register_button.click()

    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

    header_logo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PageLocators.HEADER_LOGO)
    )
    header_logo.click()

    WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))

    return unique_email, password