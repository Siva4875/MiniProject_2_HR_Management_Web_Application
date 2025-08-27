import csv
import pytest
import logging
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# Set up logger for this test file
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def read_rows():
    """
    Reads login test data from CSV file.
    Expected CSV format:
        Username,Password,Expected
        Admin,admin123,Valid
        user,wrongpass,Invalid
    """
    logger.info("Reading credentials from data/credentials.csv")
    with open("data/credentials.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    logger.info(f"Loaded {len(rows)} test rows from credentials.csv")
    return rows


@pytest.mark.regression
@pytest.mark.parametrize("row", read_rows())
def test_login_ddt(driver, row):
    """
    Data-driven login test using credentials from CSV file.
    - If Expected=Valid → Verify successful login and logout
    - If Expected=Invalid → Verify error message is displayed
    """
    username, password, expected = row["Username"], row["Password"], row["Expected"]

    logger.info(f"Starting login test with Username='{username}', Expected='{expected}'")

    # Step 1: Load login page
    lp = LoginPage(driver)
    lp.load()

    # Step 2: Perform login
    logger.info(f"Attempting login with Username='{username}'")
    lp.do_login(username, password)

    # Step 3: Validate result
    db = DashboardPage(driver)
    if expected.strip().lower() == "valid":
        logger.info("Expected valid login. Checking dashboard visibility.")
        assert db.is_logged_in(), f"Expected successful login for user '{username}'"
        logger.info("Login successful. Logging out now.")
        db.logout()
    else:
        logger.info("Expected invalid login. Checking for error message.")
        error_msg = lp.get_error()
        assert "Invalid" in error_msg, f"Expected invalid login message, got '{error_msg}'"
        logger.info("Invalid login error message verified successfully.")
