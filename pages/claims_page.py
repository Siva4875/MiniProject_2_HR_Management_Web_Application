from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import datetime
from utils.logger import get_logger   # import custom logger

logger = get_logger(__name__)  # module-level logger


class ClaimsPage(BasePage):
    """
    Page Object Model for the Claims page.
    Handles creation and submission of new claims with items.
    """

    # ---------- Locators ----------
    submit_claim = (By.XPATH, "//a[normalize-space()='Submit Claim']")
    event_dropdown = (By.XPATH, "//label[text()='Event']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    first_event = (By.XPATH, "(//div[@role='listbox' and not(contains(@style,'display: none'))]//div[@role='option'])[1]")

    currency_dropdown = (By.XPATH, "//label[text()='Currency']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    first_curr = (By.XPATH, "//div[@role='listbox']//div[@role='option'][1]")
    remarks = (By.XPATH, "//label[text()='Remarks']/../following-sibling::div//textarea")
    save_btn = (By.XPATH, "//button[normalize-space()='Create']")    
    add_item_btn = (By.XPATH, "//button[.//i[contains(@class,'plus')]]")

    expense_type_dropdown = (By.XPATH, "//label[text()='Expense Type']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    Note = (By.XPATH, "//label[text()='Note']/../following-sibling::div//textarea")
    date = (By.XPATH, "//input[@placeholder='yyyy-dd-mm'][1]")
    item_select = (By.XPATH, "//div[@role='listbox']//div[@role='option'][1]")
    amount_input = (By.XPATH, "//label[text()='Amount']/../following-sibling::div//input")
    Save_button_1 = (By.XPATH, "//button[normalize-space()='Save']")
    success_toast = (By.XPATH, "//div[contains(@class,'oxd-toast--success')]")

    # ---------- Methods ----------
    def start_claim(self, remark="Automated claim"):
        """
        Initiates and submits a new claim with one expense item.

        Args:
            remark (str): Remark text for the claim (default="Automated claim").

        Returns:
            bool: True if success toast appears, False otherwise.
        """
        logger.info("Starting a new claim process...")

        # Click Submit Claim
        logger.debug("Clicking 'Submit Claim' button.")
        self.click(self.submit_claim)

        # Select Event
        logger.debug("Selecting event: Accommodation.")
        self.click(self.event_dropdown)
        locator = (By.XPATH, "//div[@role='listbox' and not(contains(@style,'display: none'))]//div[@role='option'][normalize-space()='Accommodation']")
        self.wait_for_element(locator)
        self.click(locator)

        # Select Currency
        logger.debug("Selecting currency: Indian Rupee.")
        self.click(self.currency_dropdown)
        locator = (By.XPATH, "//div[@role='listbox' and not(contains(@style,'display: none'))]//div[@role='option'][normalize-space()='Indian Rupee']")
        self.wait_for_element(locator)
        self.click(locator)

        # Enter remarks
        logger.debug(f"Entering remarks: {remark}")
        self.type(self.remarks, remark)

        # Save main claim
        logger.debug("Clicking 'Create' to save claim.")
        self.click(self.save_btn)

        # Add an item to claim
        logger.debug("Adding an expense item to claim.")
        self.click(self.add_item_btn)

        # Select expense type if dropdown appears
        try:
            logger.debug("Selecting expense type: Accommodation.")
            self.click(self.expense_type_dropdown)
            locator = (By.XPATH, "//div[@role='listbox' and not(contains(@style,'display: none'))]//div[@role='option'][normalize-space()='Accommodation']")
            self.wait_for_element(locator)
            self.click(locator)
        except Exception as e:
            logger.warning(f"Expense type selection skipped due to: {e}")

        # Fill in amount and note
        logger.debug("Entering expense details: Amount=10, Note='Automated claim item'.")
        self.type(self.amount_input, "10")
        self.type(self.Note, "Automated claim item")

        # Add today's date
        start = datetime.date.today()
        logger.debug(f"Entering date: {start.strftime('%Y-%m-%d')}")
        self.type(self.date, start.strftime("%Y-%m-%d"))

        # Save expense item
        logger.debug("Clicking 'Save' to add expense item.")
        self.click(self.Save_button_1)

        # Validate success
        result = self.is_visible(self.success_toast)
        if result:
            logger.info("Claim created successfully")
        else:
            logger.error("Claim creation failed")
        return result
