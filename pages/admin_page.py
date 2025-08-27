from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

# Initialize logger for this page
log = get_logger(__name__)

class AdminPage(BasePage):
    """
    Page Object for the Admin module.
    Provides locators and reusable actions for managing users.
    """

    # Locators
    users_header = (By.XPATH, "//h6[text()='Users']")
    add_button = (By.XPATH, "//button[.//i[contains(@class,'plus')]] | //button[normalize-space()='Add']")
    save_button = (By.XPATH, "//button[normalize-space()='Save']")
    search_username = (By.XPATH, "//label[text()='Username']/../following-sibling::div//input")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")
    table_rows = (By.XPATH, "//div[@role='table']//div[@role='row']")

    # Add User form fields
    role_dropdown = (By.XPATH, "//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    role_option_ess = (By.XPATH, "//div[@role='listbox']//span[text()='ESS']")
    status_dropdown = (By.XPATH, "//label[text()='Status']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    status_enabled = (By.XPATH, "//div[@role='listbox']//span[text()='Enabled']")
    employee_name = (By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input")
    username = (By.XPATH, "//label[text()='Username']/../following-sibling::div//input")
    password = (By.XPATH, "//label[text()='Password']/../following-sibling::div//input")
    confirm_password = (By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div//input")
    autocomplete_option = (By.XPATH, "//div[@role='listbox']//span")
    success_toast = (By.XPATH, "//div[contains(@class,'oxd-toast--success')]")

    def open_user_mgmt(self):
        """
        Navigate to the User Management section.
        Assumes user is already on the Admin menu.
        """
        log.info("Navigating to User Management section (placeholder method).")
        pass

    def add_user(self, employee, new_username, pwd):
        """
        Add a new user in the Admin module.
        :param employee: Employee name to link user
        :param new_username: New username for the account
        :param pwd: Password for the account
        :return: True if success toast is visible, False otherwise
        """
        log.info(f"Adding new user: {new_username} for employee: {employee}")

        self.click(self.add_button)
        log.debug("Clicked 'Add' button")

        self.click(self.role_dropdown); self.click(self.role_option_ess)
        log.debug("Selected role: ESS")

        self.click(self.status_dropdown); self.click(self.status_enabled)
        log.debug("Selected status: Enabled")

        self.type(self.employee_name, employee)
        log.debug(f"Entered employee name: {employee}")

        # Select first match in autocomplete
        self.click(self.autocomplete_option)
        log.debug("Selected first employee match from autocomplete")

        self.type(self.username, new_username)
        log.debug(f"Entered username: {new_username}")

        self.type(self.password, pwd)
        self.type(self.confirm_password, pwd)
        log.debug("Entered password and confirmed password")

        self.click(self.save_button)
        log.info("Clicked 'Save' button")

        success = self.is_visible(self.success_toast)
        if success:
            log.info(f"User '{new_username}' added successfully.")
        else:
            log.error(f"Failed to add user '{new_username}'.")
        return success

    def search_user(self, uname):
        """
        Search for a user in the Admin module.
        :param uname: Username to search
        :return: True if table rows are visible (results found), False otherwise
        """
        log.info(f"Searching for user: {uname}")

        self.type(self.search_username, uname)
        log.debug(f"Entered username in search field: {uname}")

        self.click(self.search_button)
        log.debug("Clicked 'Search' button")

        result = self.is_visible(self.table_rows)
        if result:
            log.info(f"User '{uname}' found in search results.")
        else:
            log.warning(f"User '{uname}' not found.")
        return result
