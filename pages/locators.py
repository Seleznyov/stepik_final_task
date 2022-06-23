from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    Registr_Form = (By.CSS_SELECTOR, "#register_form")
    Login_Form = (By.CSS_SELECTOR, "#login_form")

class BasketLocators():
    Basket = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")

class OrderLocators():
    Order = (By.XPATH, "//div[@class='alertinner ']/strong")
    Name_Order = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")

class PricerLocators():
    Price_Basket = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    Price_Order = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")

class ProductPageLocators():
    # Не придумал другой локатор
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class GoToBasketLocators():
    Go_to_Basket = (By.XPATH, "//span[@class='btn-group']/a")
    Basket_Name = (By.XPATH, "//div[@class='page-header action']/h1")
    Message_Empty_Basket = (By.XPATH, "//div[@id='content_inner']/p")

class RegisterNewUserLocators():
    Register_Email = (By.CSS_SELECTOR, "[name='registration-email']")
    Register_Password1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    Register_Password2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    Register_Button = (By.CSS_SELECTOR, "[name='registration_submit']")