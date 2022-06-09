from .base_page import BasePage
from .locators import GoToBasketLocators
from .languages import languages

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_name_is()

    def should_be_basket_url(self):
        #  Реализуйте проверку на корректный url адрес
        assert "basket" in self.browser.current_url, "url is not correct"

    def should_be_basket_name_is(self):
        # Реализуйте проверку, что есть заголовок "Корзина" или "Basket"
        assert self.is_element_present(*GoToBasketLocators.Basket_Name), "Basket name is not presented"

    def should_not_be_basket_page(self):
        # Проверяем отсуствие ссылки на "Посмотреть корзину"
        assert self.is_not_element_present(*GoToBasketLocators.Go_to_Basket), "message is presented, but should not be"

    def basket_message_empty(self):
        lan = self.language()
        assert languages[lan] in self.browser.find_element(*GoToBasketLocators.Message_Empty_Basket).text, "сообщение не верное"
