from .base_page import BasePage
from .locators import LoginPageLocators,RegisterNewUserLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url,"url is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.Login_Form),"login_form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.Registr_Form),"Registr_Form  is not presented"

    def register_new_user(self,email, password):
        Email = self.browser.find_element(*RegisterNewUserLocators.Register_Email)
        Email.send_keys(email)
        Password1 = self.browser.find_element(*RegisterNewUserLocators.Register_Password1)
        Password1.send_keys(password)
        Password2 = self.browser.find_element(*RegisterNewUserLocators.Register_Password2)
        Password2.send_keys(password)
        button = self.browser.find_element(*RegisterNewUserLocators.Register_Button)
        button.click()