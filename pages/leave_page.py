import logging
import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Set up logger for this page
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LeavePage(BasePage):
    # Locators
    assign_leave_menu = (By.XPATH, "//a[normalize-space()='Assign Leave']")
    employee_input = (By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input")
    leave_type_dropdown = (By.XPATH, "//label[text()='Leave Type']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    first_leave_type = (By.XPATH, "//div[@role='listbox']//div[@role='option'][1]")
    from_date = (By.XPATH, "//input[@placeholder='yyyy-dd-mm'][1]")
    comments = (By.XPATH, "//label[text()='Comments']/../following-sibling::div//textarea")
    assign_btn = (By.XPATH, "//button[normalize-space()='Assign']")
    confirm_btn = (By.XPATH, "//button[normalize-space()='Ok']")
    success_toast = (By.XPATH, "//div[contains(@class,'oxd-toast--success')]")

    def assign_leave(self, employee, days=1, comment='Automated leave'):
        """
        Assign leave for an employee.
        :param employee: str - Employee name to assign leave.
        :param days: int - Number of leave days (default = 1).
        :param comment: str - Comment for leave assignment.
        :return: bool - True if success toast is visible.
        """

        logger.info("Navigating to Assign Leave menu.")
        self.click(self.assign_leave_menu)

        logger.info(f"Typing employee name: {employee}")
        self.type(self.employee_input, employee)

        # Choose the first autocomplete suggestion
        logger.info("Selecting first employee from autocomplete list.")
        from selenium.webdriver.common.by import By as _By
        self.click((_By.XPATH, "//div[@role='listbox']//span"))

        # Select leave type
        logger.info("Opening Leave Type dropdown.")
        self.click(self.leave_type_dropdown)

        locator = (By.XPATH, "//div[@role='listbox' and not(contains(@style,'display: none'))]"
                             "//div[@role='option'][normalize-space()='CAN - Personal']")
        logger.info("Waiting for leave type 'CAN - Personal' to appear.")
        self.wait_for_element(locator)

        logger.info("Selecting leave type: CAN - Personal")
        self.click(locator)

        # Date entry (From Date = Today, To Date = Today for 1-day leave)
        start = datetime.date.today()
        logger.info(f"Entering leave start date: {start.strftime('%Y-%m-%d')}")
        self.type(self.from_date, start.strftime("%Y-%m-%d"))

        logger.info(f"Entering comments: {comment}")
        self.type(self.comments, comment)

        logger.info("Clicking Assign button.")
        self.click(self.assign_btn)

        # Handle confirmation if prompt appears
        if self.is_visible(self.confirm_btn):
            logger.info("Confirmation dialog detected. Clicking OK.")
            self.click(self.confirm_btn)

        # Verify success
        success = self.is_visible(self.success_toast)
        if success:
            logger.info("Leave assignment successful. Success toast displayed.")
        else:
            logger.warning("Leave assignment might have failed. Success toast not found.")

        return success
