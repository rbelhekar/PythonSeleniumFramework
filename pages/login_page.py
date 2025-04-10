from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()=' Login ']")
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    ERROR_LABEL = (By.CSS_SELECTOR, "p.oxd-alert-content-text")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_username(self, username):
        self.do_send_keys(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.do_send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.do_click(self.LOGIN_BUTTON)

    def is_dashboard_visible(self):
        return self.is_element_visible(self.DASHBOARD_HEADER)
