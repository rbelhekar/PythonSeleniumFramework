from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time

def test_valid_login(init_driver):
    driver = init_driver
    login_page = LoginPage(driver)

    # Valid Login Test
    login_page.username_input.enter_text("Admin")
    login_page.password_input.enter_text("admin123")
    login_page.login_button.click_if_enabled()
    time.sleep(2)

    dashboard_page = DashboardPage(driver)
    assert dashboard_page.dashboard_label.visible, "Login failed: Dashboard not visible!"


def test_invalid_login(init_driver):
    driver = init_driver
    login_page = LoginPage(driver)

    login_page.username_input.enter_text("wrongAdmin")
    login_page.password_input.enter_text("wrongPasswd")
    login_page.login_button.click_if_enabled()
    time.sleep(2)

    assert login_page.error_label.text == "Invalid credentials", "Error Text does not Match!"
