from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

# @pytest.mark.parametrize('link', ["?promo=offer0","?promo=offer1","?promo=offer2","?promo=offer3",
#                                   "?promo=offer4","?promo=offer5","?promo=offer6",
#                                   pytest.param("?promo=offer7", marks=pytest.mark.xfail),"?promo=offer8","?promo=offer9"])

# def test_guest_can_add_product_to_basket(browser,link):
#     product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}"
#     # link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     # link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, product_link)
#     page.open()
#     page.should_not_be_success_message()
#     page.add_basket()
#     page.solve_quiz_and_get_code()
#     page.should_item_added_to_cart()
#     page.should_price()
#     page.should_is_disappeared

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, product_link)
    page.open()
    page.add_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, product_link)
    page.open()
    page.add_basket()
    page.should_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, product_link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page (browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/"
    page = ProductPage(browser, product_link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.go_to_basket()
    basket_page.basket_message_empty()