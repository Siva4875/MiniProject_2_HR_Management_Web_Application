from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from utils import config
from utils import logger
from utils.logger import get_logger
from selenium.webdriver.common.keys import Keys

# Initialize logger for this module
log = get_logger(__name__)

class BasePage:
    def __init__(self, driver):
        """
        Base class for all page objects.
        Provides reusable Selenium utility functions.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)  # Explicit wait for elements

    def open(self, url):
        """Open a given URL in the browser."""
        log.info(f"Opening URL: {url}")
        self.driver.get(url)

    def click(self, locator):
        """Click an element, falling back to JavaScript if intercepted."""
        try:
            log.info(f"Clicking element: {locator}")
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except ElementClickInterceptedException:
            log.warning(f"Click intercepted, using JavaScript click for: {locator}")
            elem = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", elem)

    def wait_for_element(self, locator, timeout: int = 10):
        """Wait until an element is clickable, return the element or None."""
        try:
            log.info(f"Waiting for element to be clickable: {locator} (timeout={timeout})")
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            log.error(f"Timeout: Element not clickable -> {locator}")
            return None

    def text_of(self, locator):
        """Get the visible text of an element."""
        log.info(f"Retrieving text from element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        """Check if an element is visible on the page."""
        try:
            log.info(f"Checking visibility of element: {locator}")
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            log.warning(f"Element not visible: {locator}")
            return False

    def exists(self, locator):
        """Check if an element exists in the DOM (without waiting)."""
        try:
            log.info(f"Checking existence of element: {locator}")
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            log.warning(f"Element does not exist: {locator}")
            return False

    def type(self, locator, text, clear_first=True):
        """
        Type text into an input field.
        - Clears the field before typing if `clear_first=True`.
        - Uses multiple fallbacks to ensure input is cleared.
        """
        log.info(f"Typing text into element {locator}: '{text}'")
        element = self.wait_for_element(locator)

        if clear_first:
            try:
                log.debug(f"Clearing input field before typing: {locator}")
                element.clear()  # normal clear
                if element.get_attribute("value"):  
                    # if still not cleared, force with CTRL+A + DELETE
                    log.debug("Input not cleared, forcing with CTRL+A + DELETE")
                    element.send_keys(Keys.CONTROL + "a")
                    element.send_keys(Keys.DELETE)
                # final fallback: JS clear
                if element.get_attribute("value"):
                    log.debug("Final fallback: clearing with JavaScript")
                    self.driver.execute_script("arguments[0].value = '';", element)
            except Exception as e:
                log.error(f"Error clearing input field: {locator} | {e}")
                self.driver.execute_script("arguments[0].value = '';", element)

        element.send_keys(text)
        log.info(f"Successfully typed text into element {locator}")
        return True
