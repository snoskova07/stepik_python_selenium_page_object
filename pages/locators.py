from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    BOOK_NAME_IN_GREEN_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]//strong")
    BOOK_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    #BOOK_PRICE_IN_BASKET = (By.XPATH, "//div[@class='basket-mini pull-right hidden-xs']")
    BOOK_PRICE_IN_BASKET = (By.XPATH, "//div[@class='alertinner ']//p//strong")


