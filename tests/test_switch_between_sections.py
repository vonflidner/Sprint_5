from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from urls import MAIN_URL


def test_switch_between_sections(driver):
    driver.get(MAIN_URL)

    fillings_title_element = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located(PageLocators.FILLINGS_TITLE)
    )
    driver.execute_script("arguments[0].scrollIntoView();", fillings_title_element)
    fillings_section_class = driver.find_element(*PageLocators.FILLINGS_SECTION).get_attribute("class")
    assert 'tab_tab_type_current__2BEPc' in fillings_section_class

    sauce_title_element = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located(PageLocators.SAUCE_TITLE)
    )
    driver.execute_script("arguments[0].scrollIntoView();", sauce_title_element)
    sauce_section_class = driver.find_element(*PageLocators.SAUCE_SECTION).get_attribute("class")
    assert 'tab_tab_type_current__2BEPc' in sauce_section_class

    bulki_title_element = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located(PageLocators.BULKI_TITLE)
    )
    driver.execute_script("arguments[0].scrollIntoView();", bulki_title_element)
    bulki_section_class = driver.find_element(*PageLocators.BULKI_SECTION).get_attribute("class")
    assert 'tab_tab_type_current__2BEPc' in bulki_section_class
