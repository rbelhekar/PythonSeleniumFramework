class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        """Return the title of the current page."""
        return self.driver.title

    def get_url(self):
        """Return the current URL."""
        return self.driver.current_url

    def refresh(self):
        """Refresh the current page."""
        self.driver.refresh()

    def go_back(self):
        """Navigate back in browser history."""
        self.driver.back()

    def go_forward(self):
        """Navigate forward in browser history."""
        self.driver.forward()

    def scroll_to_top(self):
        """Scroll to the top of the page."""
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_for_title(self, title, timeout=10):
        """Wait until the page title matches."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        WebDriverWait(self.driver, timeout).until(EC.title_is(title))

    def wait_for_url_contains(self, text, timeout=10):
        """Wait until the URL contains a given text."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))
