from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from .. import _widgets
from . import _locators

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # Open URL
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Initialize elements
        self.username_input = _widgets.Textbox(driver,_locators.USERNAME_INPUT)
        self.password_input = _widgets.Textbox(driver, _locators.PASSWORD_INPUT)
        self.login_button = _widgets.Button(driver, _locators.LOGIN_BUTTON)
        self.error_label = _widgets.Widget(driver, _locators.ERROR_LABEL)

    def login_as(self, username, password):
        self.username_input.enter_text(username)
        self.password_input.enter_text(password)
        self.login_button.click()

        # Wait until the Dashboard is loaded
        DashboardPage(self.driver).wait_until_loaded()

        return DashboardPage(self.driver)

    '''def enter_username(self, username):
        self.do_send_keys(self.username_input, username)

    def enter_password(self, password):
        self.do_send_keys(self.password_input, password)

    def click_login(self):
        self.do_click(self.LOGIN_BUTTON)

    def is_dashboard_visible(self):
        return self.is_element_visible(self.DASHBOARD_HEADER)'''
