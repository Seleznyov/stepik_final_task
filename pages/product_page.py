from .base_page import BasePage
from .locators import BasketLocators,OrderLocators,PricerLocators,ProductPageLocators,BasePageLocators
from selenium.common.exceptions import NoAlertPresentException

import math

class ProductPage(BasePage):
    def add_basket(self):
        Basket = self.browser.find_element(*BasketLocators.Basket)
        Basket.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        # Код нужен:) поэтму оставляю!
        # alert = self.browser.switch_to.alert
        # alert.accept()
        # try:
        #     alert = self.browser.switch_to.alert
        #     # alert_text = alert.text
        #     # print(f"Your code: {alert_text}")
        #     alert.accept()
        # except NoAlertPresentException:
        #     print("No second alert presented")

    def should_item_added_to_cart(self):
        order = self.browser.find_element(*OrderLocators.Order)
        test_result = order.text
        name_order = self.browser.find_element(*OrderLocators.Name_Order)
        test_name = name_order.text
        print(test_name)
        assert test_name == test_result, "имя заказа не совпадает "+" Актуальный "+test_result+" Ожидаемый "+test_name

    def should_price(self):
        basket = self.browser.find_element(*PricerLocators.Price_Basket)
        Price_Basket = basket.text
        order = self.browser.find_element(*PricerLocators.Price_Order)
        Price_Order = order.text
        print(Price_Basket)
        assert Price_Basket == Price_Order, "Стоимость разная"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

