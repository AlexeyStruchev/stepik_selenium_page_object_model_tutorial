from faker import Faker
from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self):
        self.fill_email()
        self.fill_password()
        self.click_register_button()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login"), "login word is present in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is present"

    def fill_email(self):
        fake = Faker()
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(fake.email())

    def fill_password(self):
        fake = Faker()
        password = fake.password()
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)

    def click_register_button(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
