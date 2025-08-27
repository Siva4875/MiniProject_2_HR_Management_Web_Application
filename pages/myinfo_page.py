import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Set up logger for this page
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class MyInfoPage(BasePage):
    """
    Page Object for the 'My Info' section in OrangeHRM.
    Provides methods to navigate and validate subsections in the sidebar.
    """

    # Page locators
    header = (By.XPATH, "//h6[contains(@class,'orangehrm-main-title')]")

    def section(self, name):
        """
        Dynamically generates the locator for sidebar sections based on name.
        :param name: str - Section name (e.g., 'Personal Details', 'Contact Details')
        :return: tuple - Locator for the section link
        """
        logger.info(f"Generating locator for section: {name}")
        return (By.XPATH, f"//a[normalize-space()='{name}']")

    def open_section(self, name):
        """
        Clicks on a sidebar section and verifies its header is visible.
        :param name: str - Section name
        :return: bool - True if header is visible after navigation, else False
        """
        logger.info(f"Clicking on sidebar section: {name}")
        self.click(self.section(name))

        logger.info("Checking if section header is visible.")
        return self.is_visible(self.header)
