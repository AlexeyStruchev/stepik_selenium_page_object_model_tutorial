import pytest
from pages.product_page import ProductPage


@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    order_page = ProductPage(browser, link, 5)
    order_page.open()
    order_page.basket_popup_message_and_price_should_be_equal_to_title_message_and_price()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    order_page = ProductPage(browser, link)
    order_page.open()
    order_page.add_to_basket()
    order_page.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    order_page = ProductPage(browser, link)
    order_page.open()
    order_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    order_page = ProductPage(browser, link)
    order_page.open()
    order_page.add_to_basket()
    order_page.should_element_disapper()

