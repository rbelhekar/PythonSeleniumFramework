from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Widget:
    def __init__(self, driver, by_locator, timeout=10):
        self.driver = driver
        self.by_locator = by_locator
        self.wait = WebDriverWait(driver, timeout)

    @property
    def element(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.by_locator))
        except TimeoutException:
            print(f"[Widget] Element {self.by_locator} not found.")
            return None

    @property
    def visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.by_locator)).is_displayed()
        except TimeoutException:
            return False

    @property
    def enabled(self):
        el = self.element
        return el.is_enabled() if el else False

    @property
    def text(self):
        el = self.element
        return el.text if el else ""

    @property
    def tooltip(self):
        el = self.element
        return el.get_attribute("title") if el else ""

    def click(self):
        el = self.wait.until(EC.element_to_be_clickable(self.by_locator))
        el.click()

    def hover(self):
        el = self.element
        if el:
            ActionChains(self.driver).move_to_element(el).perform()

    def drag_and_drop(self, target_element):
        source = self.element
        target = target_element.element if isinstance(target_element, Widget) else target_element
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def scroll_into_view(self):
        el = self.element
        if el:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
