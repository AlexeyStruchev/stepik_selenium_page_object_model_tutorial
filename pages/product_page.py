from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def basket_popup_message_and_price_should_be_equal_to_title_message_and_price(self):
        self.cclick_add_to_basket_button()
        self.product_title_equal_to_basket_popup_title()
        self.product_price_is_equal_to_basket_popup_price()

    def click_add_to_basket_button(self):
        add_to_basket_button = self.is_element_present(*ProductPageLocators.product_add_to_basket_button)
        add_to_basket_button.click()
    def product_title_equal_to_basket_popup_title(self):
        basket_popup_title_text = self.is_element_present(*ProductPageLocators.product_basket_popup_message).text
        product_title = "The shellcoder's handbook"
        assert basket_popup_title_text == product_title,\
            f'A basket popup title < {basket_popup_title_text} > has to be equal to a product title < {product_title} >'

    def product_price_is_equal_to_basket_popup_price(self):
        basket_popup_price = self.is_element_present(*ProductPageLocators.product_basket_popup_price)
        assert basket_popup_price.text == '£9.99', 'Basket popup price is equal to product price'

    def product_price_is_equal_to_basket_popup_price(self):
        basket_popup_price_text = self.is_element_present(*ProductPageLocators.product_basket_popup_price).text
        product_price = "£9.99"
        assert basket_popup_price_text == product_price,\
            f'A basket popup price < {basket_popup_price_text} > has to be equal to a product price < {product_price} >'