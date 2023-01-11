from pages.base_page import BasePage
from pages.locators import ProductPageLocators


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
        add_to_basket_button = self.is_element_present(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_title(self):
        return self.is_element_present(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.is_element_present(*ProductPageLocators.PRODUCT_PRICE).text

    def product_title_equal_to_basket_popup_title(self, product_title_):
        basket_popup_title_text = self.is_element_present(*ProductPageLocators.PRODUCT_BASKET_POPUP_TITLE).text
        assert product_title_  == basket_popup_title_text,\
            f'A basket popup title < {basket_popup_title_text} > has to be equal to a product title < {product_title_} >'

    def product_price_is_equal_to_basket_popup_price(self, product_price_):
        basket_popup_price_text = self.is_element_present(*ProductPageLocators.PRODUCT_BASKET_POPUP_PRICE).text
        assert product_price_  == basket_popup_price_text, \
            f'A basket popup price < {basket_popup_price_text} > has to be equal to a product price < {product_price_} >'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_element_disapper(self):
        assert self.is_disappeared(*ProductPageLocators.DISAPPERED_ELEMENT), \
            "Success message is not dissapeared, but should be"

    def add_to_basket(self):
        self.click_add_to_basket_button()