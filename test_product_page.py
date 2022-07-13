from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time
import faker

@pytest.mark.parametrize('link', ["?promo=offer0","?promo=offer1","?promo=offer2","?promo=offer3",
                                  "?promo=offer4","?promo=offer5","?promo=offer6",
                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),"?promo=offer8","?promo=offer9"])

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser,link):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}"
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()
    page.add_basket()
    page.solve_quiz_and_get_code()
    page.should_item_added_to_cart()
    page.should_price()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, product_link)
    page.open()
    page.add_basket()
    page.should_not_be_success_message()


@pytest.mark.add_to_basket
class TestAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        yield
        pass
    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    # Код нужен:) поэтому и не удаляю !!!
    # def test_guest_cant_see_success_message(browser):
    #     product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    #     page = ProductPage(browser, product_link)
    #     page.open()
    #     page.should_not_be_success_message()

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

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, product_link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.go_to_login_page()
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page (browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/"
    page = ProductPage(browser, product_link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.go_to_basket()
    basket_page.basket_message_empty()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        f = faker.Faker()
        email = f.email()
        page.register_new_user(email="test"+email, password="password_test")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.parametrize('link', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3",
                                      "?promo=offer4", "?promo=offer5", "?promo=offer6",
                                      pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8","?promo=offer9"])

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser, link):
        product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}"
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()
        page.add_basket()
        page.solve_quiz_and_get_code()
        page.should_item_added_to_cart()
        page.should_price()