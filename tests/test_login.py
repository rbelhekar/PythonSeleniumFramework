from pages import LoginPage
import time

def test_valid_login(init_driver):
    driver = init_driver
    login_page = LoginPage(driver)

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    time.sleep(2)

    assert login_page.is_dashboard_visible(), "Login failed: Dashboard not visible!"

def test_invalid_login(init_driver):
    driver = init_driver
    login_page = LoginPage(driver)

    login_page.enter_username("wrongAdmin")
    login_page.enter_password("wrongPasswd")
    login_page.click_login()
    time.sleep(2)

    assert login_page.get_element_text(login_page.ERROR_LABEL) == "Invalid credentials", "Error Text does not Match!"
