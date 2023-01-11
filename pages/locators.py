from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET = (By.CLASS_NAME, "btn-group")
    USER_ICON = (By.CLASS_NAME, "icon-user")

class LoginPageLocators():
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")

class ProductPageLocators():
    DISAPPERED_ELEMENT = (By.CSS_SELECTOR, '#messages > div:nth-child(2) > div')
    PRODUCT_ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_BASKET_POPUP_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > div > p > strong')
    PRODUCT_BASKET_POPUP_TITLE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')

class BasketPageLocators():
    BASKET_IS_EMPTY = (By.CLASS_NAME, 'col-sm-6')
    BASKET_IS_EMPTY_TEXT = (By.ID, 'content_inner')
