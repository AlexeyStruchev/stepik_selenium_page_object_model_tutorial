from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def test_basket_title_message_and_price(self):
        self.product_title_equal_to_basket_popup_title()
        self.product_price_is_equal_to_basket_popup_price()

    def product_title_equal_to_basket_popup_title(self):
        basket_popup_title = self.find_element_simple(*ProductPageLocators.product_basket_popup_message)
        assert basket_popup_title.text == "The shellcoder's handbook", 'Basket popup title is equal to product title'

    def product_price_is_equal_to_basket_popup_price(self):
        basket_popup_price = self.is_element_present(*ProductPageLocators.product_basket_popup_price).text
        assert basket_popup_price == '£9.99', 'Basket popup price is equal to product price'