from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestLanguage:
    def test_add_to_basket(self, browser):
        browser.get(link)
        login_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-add-to-basket'))
        )
        time.sleep(5)
        assert login_button, "Корзина не найдена"
