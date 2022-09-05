from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_cart(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()

    def get_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        return book_name.text

    def should_be_cart_url(self):
        # реализуйте проверку на корректный url адрес
        assert '/accounts/login/' in self.browser.current_url, "Cart URL is wrong"

    def should_have_correct_book_name_after_adding_book_to_cart(self):
        name = self.get_book_name()
        assert name in self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_GREEN_MESSAGE).text, "The book " \
                                                                                                        "name is not " \
                                                                                                        "matched "
