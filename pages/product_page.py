from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def basket_popup_message_and_price_should_be_equal_to_title_message_and_price(self):
        # self.should_be_promo_parameter_in_url(self.get_parameter_from_url(), "promo=newYear2019")
        self.click_add_to_basket_button()
        self.solve_quiz_and_get_code()
        self.product_title_equal_to_basket_popup_title(self.get_product_title())
        self.product_price_is_equal_to_basket_popup_price(self.get_product_price())

    def get_parameter_from_url(self):
        separated_list = self.browser.current_url.split('?')
        return str(separated_list[1])

    def should_be_login_url(self):
        assert self.browser.current_url.find("login"), "login word is present in url"


    def should_be_promo_parameter_in_url(self, url_parameter_, check_parameter):
        assert url_parameter_ == check_parameter,\
            f"Parameter < {url_parameter_} > has to be equal to < {check_parameter} >"

    def click_add_to_basket_button(self):
        add_to_basket_button = self.is_element_present(*ProductPageLocators.product_add_to_basket_button)
        add_to_basket_button.click()

    def get_product_title(self):
        return self.is_element_present(*ProductPageLocators.product_title).text

    def get_product_price(self):
        return self.is_element_present(*ProductPageLocators.product_price).text

    def product_title_equal_to_basket_popup_title(self, product_title_):
        basket_popup_title_text = self.is_element_present(*ProductPageLocators.product_basket_popup_title).text
        assert product_title_  == basket_popup_title_text,\
            f'A basket popup title < {basket_popup_title_text} > has to be equal to a product title < {product_title_} >'

    def product_price_is_equal_to_basket_popup_price(self, product_price_):
        basket_popup_price_text = self.is_element_present(*ProductPageLocators.product_basket_popup_price).text
        assert product_price_  == basket_popup_price_text, \
            f'A basket popup price < {basket_popup_price_text} > has to be equal to a product price < {product_price_} >'