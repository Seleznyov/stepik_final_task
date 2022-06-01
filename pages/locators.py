from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    Registr_Form = (By.CSS_SELECTOR, "#register_form")
    Login_Form = (By.CSS_SELECTOR, "#login_form")

class BasketLocators():
    Basket = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")

class OrderLocators():
    Order = (By.CSS_SELECTOR, "[class='alertinner ']")
    Name_Order = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")

class PricerLocators():
    Price_Basket = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    Price_Order = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
