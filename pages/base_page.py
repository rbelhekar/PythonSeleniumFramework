from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def do_click(self, by_locator):
        try:
            self.wait.until(EC.element_to_be_clickable(by_locator)).click()
        except TimeoutException:
            print(f"Element {by_locator} not clickable!")

    def do_send_keys(self, by_locator, text):
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except TimeoutException:
            print(f"Element {by_locator} not visible to send keys!")

    def get_element_text(self, by_locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            return element.text
        except TimeoutException:
            print(f"Element {by_locator} not visible to get text!")

    def is_element_visible(self, by_locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator)).is_displayed()
        except TimeoutException:
            return False
