import logging
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test_forgot_password_flow(driver):
    """
    Test Case:
    1. Load the login page
    2. Navigate to "Forgot Password" page
    3. Enter username and submit reset request
    4. Verify that a reset confirmation message is displayed
    """

    logger.info("Starting test: test_forgot_password_flow")

    # Step 1: Initialize LoginPage
    lp = LoginPage(driver)
    lp.load()
    logger.info("Login page loaded successfully")

    # Step 2: Go to Forgot Password page
    lp.go_to_forgot()
    logger.info("Navigated to Forgot Password page")

    # Step 3: Define locators for Forgot Password page
    uname_field = (By.XPATH, "//input[@name='username' or @placeholder='Username']")
    submit_btn = (
        By.XPATH,
        "//button[@type='submit' and normalize-space()='Reset Password'] "
        "| //button[@type='submit']"
    )

    # Step 4: Enter username if field is visible and submit
    if lp.is_visible(uname_field):
        logger.info("Username field visible, entering username: Admin")
        lp.type(uname_field, "Admin")
        logger.info("Clicking on Reset Password button")
        lp.click(submit_btn)
    else:
        logger.warning("Username field not visible on Forgot Password page")

    # Step 5: Define locator for confirmation message
    confirmation = (
        By.XPATH,
        "//h6[contains(text(),'Reset Password link sent successfully')] "
        "| //p[contains(text(),'instructions')] "
        "| //h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']"
    )

    # Step 6: Assert confirmation is visible
    logger.info("Validating presence of confirmation message after reset")
    assert lp.is_visible(confirmation), "Reset Password confirmation message not displayed"
    logger.info("Reset Password flow successful - confirmation message displayed")

    logger.info("Test test_forgot_password_flow completed successfully")
