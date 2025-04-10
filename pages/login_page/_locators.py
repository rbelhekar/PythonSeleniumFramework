from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
LOGIN_BUTTON = (By.XPATH, "//button[text()=' Login ']")
ERROR_LABEL = (By.CSS_SELECTOR, "p.oxd-alert-content-text")