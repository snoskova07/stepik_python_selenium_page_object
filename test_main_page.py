import time
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser, user_language):
    link = f"http://selenium1py.pythonanywhere.com/{user_language}"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()
    time.sleep(2)
