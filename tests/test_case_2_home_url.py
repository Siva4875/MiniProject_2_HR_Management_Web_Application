import logging
from utils import config
from pages.login_page import LoginPage

# Set up logger for this test file
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test_home_url_accessible(driver):
    """
    Test to verify that the home (login) page is accessible.
    Steps:
      1. Load the login page.
      2. Verify that the current URL starts with the BASE_URL.
    """
    logger.info("Starting test: test_home_url_accessible")

    # Step 1: Load login page
    lp = LoginPage(driver)
    lp.load()
    logger.info(f"Opened login page at: {driver.current_url}")

    # Step 2: Validate that the base URL is accessible
    assert driver.current_url.startswith(config.BASE_URL), \
        f"Home URL not accessible. Current URL: {driver.current_url}"
    
    logger.info("Home URL is accessible and matches the BASE_URL")
