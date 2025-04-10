from pages.base_page import BasePage
from .. import _widgets
from . import _locators

class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # Open URL
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

        # Initialize elements
        self.dashboard_label = _widgets.Widget(driver, _locators.DASHBOARD_HEADER)

    def wait_until_loaded(self):
        return self.dashboard_label.visible