import logging
from pages.login_page import LoginPage

# Configure logger for this test file
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test_login_fields_present(driver):
    """
    Test to verify that the login page has required fields visible:
      - Username field
      - Password field
    """

    logger.info("Starting test: test_login_fields_present")

    # Step 1: Load the login page
    lp = LoginPage(driver)
    lp.load()
    logger.info("Login page loaded successfully")

    # Step 2: Verify that username field is visible
    assert lp.is_visible(lp.username), "Username field not visible on login page"
    logger.info("Username field is visible")

    # Step 3: Verify that password field is visible
    assert lp.is_visible(lp.password), "Password field not visible on login page"
    logger.info("Password field is visible")

    logger.info("Test test_login_fields_present completed successfully")
