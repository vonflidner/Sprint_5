from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from urls import MAIN_URL


def test_switch_between_sections(driver):
    driver.get(MAIN_URL)

    fillings_title_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(PageLocators.FILLINGS_TITLE)
    )
    driver.execute_script("arguments[0].scrollIntoView();", fillings_title_element)

    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element_attribute(
            PageLocators.FILLINGS_SECTION, "class", "tab_tab_type_current"
        )
    )
    fillings_section_class = driver.find_element(*PageLocators.FILLINGS_SECTION).get_attribute("class")
    assert 'tab_tab_type_current' in fillings_section_class

    sauce_title_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(PageLocators.SAUCE_TITLE)
    )
    driver.execute_script("arguments[0].scrollIntoView();", sauce_title_element)

    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element_attribute(
            PageLocators.SAUCE_SECTION, "class", "tab_tab_type_current"
        )
    )
    sauce_section_class = driver.find_element(*PageLocators.SAUCE_SECTION).get_attribute("class")
    assert 'tab_tab_type_current' in sauce_section_class

    bulki_title_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(PageLocators.BULKI_TITLE)
    )
    driver.execute_script("arguments[0].scrollIntoView();", bulki_title_element)

    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element_attribute(
            PageLocators.BULKI_SECTION, "class", "tab_tab_type_current"
        )
    )
    bulki_section_class = driver.find_element(*PageLocators.BULKI_SECTION).get_attribute("class")
    assert 'tab_tab_type_current' in bulki_section_class
