import logging
from pages.dashboard_page import DashboardPage
from pages.claims_page import ClaimsPage

# Configure logger for this test module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test_initiate_claim(login_as_admin):
    """
    Test Case:
    1. Login as admin (via fixture)
    2. Navigate to 'Claim' section
    3. Initiate a new claim
    4. Verify that the claim was submitted successfully
    """

    logger.info("Starting test: test_initiate_claim")

    # Step 1: Get DashboardPage instance from fixture (already logged in as Admin)
    db: DashboardPage = login_as_admin
    logger.info("Logged in as Admin successfully")

    # Step 2: Navigate to "Claim" section
    db.open_menu("Claim")
    logger.info("Navigated to 'Claim' section")

    # Step 3: Initialize ClaimsPage
    cp = ClaimsPage(db.driver)

    # Step 4: Attempt to start a claim
    logger.info("Attempting to initiate a new claim")
    assert cp.start_claim(), "Claim submission failed"

    logger.info("Claim successfully initiated")
    logger.info("Test test_initiate_claim completed successfully")
