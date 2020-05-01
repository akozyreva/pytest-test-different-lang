# there will be test
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_name_btn_depends_browser_lang(browser):
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
        expected_conditions.
        visibility_of_element_located(
            (By.CSS_SELECTOR, "button.btn-add-to-basket")
            )
    )
    assert button, "Button wasn't found"
    print(button.text)