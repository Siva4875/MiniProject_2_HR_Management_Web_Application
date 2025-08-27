import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Set up logger for this page
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DashboardPage(BasePage):
    # Locators
    user_dropdown = (By.XPATH, "//p[contains(@class,'oxd-userdropdown-name')]")
    logout_link = (By.XPATH, "//a[text()='Logout']")

    # Dynamic locator for menu items by visible text
    def menu_item(self, name):
        return (By.XPATH, f"//span[text()='{name}']")

    def is_logged_in(self):
        """
        Check if the user dropdown (profile) is visible, 
        which indicates a successful login.
        """
        logger.info("Checking if user is logged in by verifying visibility of user dropdown.")
        return self.is_visible(self.user_dropdown)

    def open_menu(self, name):
        """
        Open a menu item by its visible text.
        :param name: str - The name of the menu item (e.g., 'Admin', 'PIM').
        """
        logger.info(f"Opening menu item: {name}")
        self.click(self.menu_item(name))

    def logout(self):
        """
        Perform logout action by expanding the user dropdown 
        and clicking the Logout link.
        """
        logger.info("Clicking on user dropdown to expand options.")
        self.click(self.user_dropdown)

        logger.info("Clicking on Logout link.")
        self.click(self.logout_link)
