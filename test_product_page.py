from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
   link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
   link2 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
   page = ProductPage(browser,link1)
   page.open()
   page.add_basket()
   page.solve_quiz_and_get_code()
   page.should_item_added_to_cart()
   page.should_price()