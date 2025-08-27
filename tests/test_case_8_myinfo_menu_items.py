import logging
from pages.dashboard_page import DashboardPage
from pages.myinfo_page import MyInfoPage

# Configure logger for this test
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test_myinfo_sections(login_as_admin):
    """
    Test Case:
    1. Login as admin (via fixture)
    2. Navigate to 'My Info' section
    3. Verify that all expected sub-sections can be opened
    """

    logger.info("Starting test: test_myinfo_sections")

    # Step 1: Get DashboardPage instance from fixture
    db: DashboardPage = login_as_admin
    logger.info("Logged in as Admin successfully")

    # Step 2: Navigate to "My Info"
    db.open_menu("My Info")
    logger.info("Navigated to 'My Info' section")

    # Step 3: Initialize MyInfoPage
    mi = MyInfoPage(db.driver)

    # Expected sections in My Info
    sections = [
        "Personal Details",
        "Contact Details",
        "Emergency Contacts",
        "Dependents",
        "Immigration"
    ]

    # Step 4: Loop through each section and verify
    for sec in sections:
        logger.info(f"Checking if section '{sec}' can be opened")
        assert mi.open_section(sec), f"Section {sec} did not open"
        logger.info(f"Section '{sec}' opened successfully")

    logger.info("Test test_myinfo_sections completed successfully")
