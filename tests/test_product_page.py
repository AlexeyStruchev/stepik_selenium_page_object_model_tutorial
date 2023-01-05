from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    order_page = ProductPage(browser, link, 5)
    order_page.open()
    order_page.basket_popup_message_and_price_should_be_equal_to_title_message_and_price()

