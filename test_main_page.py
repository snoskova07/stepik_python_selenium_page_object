import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser, user_language):
    link = f"http://selenium1py.pythonanywhere.com/{user_language}"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()
    time.sleep(3)


def test_guest_should_see_login_link(browser, user_language):
    link = f"http://selenium1py.pythonanywhere.com/{user_language}"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
