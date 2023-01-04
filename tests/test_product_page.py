from pages.product_page import ProductPage


def test_basket_title_message_and_price(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"
    order_page = ProductPage(browser, link, 5)
    order_page.product_title_equal_to_basket_popup_title()
