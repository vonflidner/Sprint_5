from selenium.webdriver.common.by import By


class PageLocators:
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Registration Name Field

    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Registration Email Field

    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")  # Registration Password Field

    SUBMIT_BUTTON = (By.XPATH,
                     "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                     "button_button_size_medium__3zxIa']")  # (Registration or Entry) Submit Button

    ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")  # Registration Error Message

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  # Personal Account Button

    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")  # Restore Password Button -
    # Login form

    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Make Order Button

    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Personal Account Button

    HEADER_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a[@href='/']")  # Header Logo WIth MAIN_URL

    ENTER_LOGIN_FORM = (By.XPATH, "//a[text()='Войти']") # Enter Login Form

    CONSTRUCTOR_BUTTON = (By.XPATH, "//ul[@class='AppHeader_header__list__3oKJj']//a[@href='/']")  # Constructor
    # Button in Personal Account

    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")  # Personal Account Exit Button

    BULKI_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Булки']]") # Bulki Section button

    SAUCE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Соусы']]") # Sauce Section Button

    FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Начинки']]") # Fillings Section Button

    BULKI_TITLE = (By.XPATH, "//h2[contains(text(),'Булки')]")

    SAUCE_TITLE = (By.XPATH, "//h2[contains(text(),'Соусы')]")

    FILLINGS_TITLE = (By.XPATH, "//h2[contains(text(),'Начинки')]")


