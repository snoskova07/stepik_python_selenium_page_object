from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_cart(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()


    def should_be_cart_url(self):
        # реализуйте проверку на корректный url адрес
        assert '/accounts/login/' in self.browser.current_url, "Cart URL is wrong"

    def get_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        return book_name.text


    def should_have_correct_book_name_after_adding_book_to_cart(self):
        name = self.get_book_name()
        assert name == self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_GREEN_MESSAGE).text, "The book name is not matched"

    def get_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return book_price.text

    def should_have_correct_price_after_adding_to_cart(self):
        price = self.get_book_price()
        price_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET).text
        print(price)
        print(price_in_basket)
        assert price == price_in_basket, "The book price is wrong, price is " + price + "price in basket = " + price_in_basket
