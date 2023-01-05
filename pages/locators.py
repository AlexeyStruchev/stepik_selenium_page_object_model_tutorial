from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form = (By.ID, "login_form")
    login_email = (By.ID, "id_login-username")
    login_password = (By.ID, "id_login-password")
    register_form = (By.ID, "register_form")
    register_email = (By.ID, "id_registration-email")
    register_password = (By.ID, "id_registration-password1")
    register_confirm_password = (By.ID, "id_registration-password2")

class ProductPageLocators():
    product_add_to_basket_button = (By.CLASS_NAME, 'btn-add-to-basket')
    product_basket_popup_message = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    product_basket_popup_price = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > div > p > strong')