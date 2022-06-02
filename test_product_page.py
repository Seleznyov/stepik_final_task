from .pages.product_page import ProductPage
import pytest
import time

@pytest.mark.parametrize('link', ["?promo=offer0","?promo=offer1","?promo=offer2","?promo=offer3",
                                  "?promo=offer4","?promo=offer5","?promo=offer6",
                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),"?promo=offer8","?promo=offer9"])

def test_guest_can_add_product_to_basket(browser,link):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}"
    # link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, product_link)
    page.open()
    page.add_basket()
    page.solve_quiz_and_get_code()
    page.should_item_added_to_cart()
    page.should_price()