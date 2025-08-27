import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import config

# Set up logger for this page
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LoginPage(BasePage):
    # Locators
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")
    error_banner = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')] "
                              "| //p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    forgot_link = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")

    def load(self):
        """
        Load the login page.
        """
        logger.info(f"Opening login page: {config.BASE_URL}")
        self.open(config.BASE_URL)

    def do_login(self, user, pwd):
        """
        Perform login with provided credentials.
        :param user: str - Username
        :param pwd: str - Password
        """
        logger.info(f"Entering username: {user}")
        self.type(self.username, user)

        logger.info("Entering password.")
        self.type(self.password, pwd)

        logger.info("Clicking on Login button.")
        self.click(self.login_btn)

    def go_to_forgot(self):
        """
        Navigate to the 'Forgot Password' page.
        """
        logger.info("Clicking on 'Forgot Password' link.")
        self.click(self.forgot_link)

    def get_error(self):
        """
        Get error message displayed on failed login.
        :return: str - Error message if visible, else empty string
        """
        logger.info("Checking for error banner.")
        if self.is_visible(self.error_banner):
            error_msg = self.text_of(self.error_banner)
            logger.warning(f"Login failed with error: {error_msg}")
            return error_msg
        logger.info("No error banner displayed.")
        return ""
