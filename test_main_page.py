import time
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser, user_language):
    link = f"http://selenium1py.pythonanywhere.com/{user_language}"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    time.sleep(5)
