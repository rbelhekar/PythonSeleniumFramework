import pytest
from utils import DriverFactory

@pytest.fixture(scope="function")
def init_driver():
    driver = DriverFactory.get_driver("chrome")  # Can switch to 'firefox' if needed
    yield driver
    driver.quit()
