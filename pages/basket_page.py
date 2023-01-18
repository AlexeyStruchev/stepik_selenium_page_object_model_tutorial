from pages.base_page import BasePage
from pages.locators import BasketPageLocators
from pages.locators import MainPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Basket is not empty but should be"

    def should_be_basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "Basket has no empty text but should be"

    def should_be_basket_is_not_empty_element(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "Basket is empty but should not be"
