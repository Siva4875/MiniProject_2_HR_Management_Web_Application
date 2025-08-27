import logging
import pytest
from pages.dashboard_page import DashboardPage

# Configure logger for this test file
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.mark.smoketest
def test_main_menu_items_visible_clickable(login_as_admin):
    """
    Smoke Test:
    Verify that all main menu items are visible on the Dashboard
    and can be clicked successfully by an admin user.
    """

    logger.info("Starting test: test_main_menu_items_visible_clickable")

    # Use the fixture to get an already logged-in DashboardPage instance
    db: DashboardPage = login_as_admin
    logger.info("Admin login successful, DashboardPage loaded")

    # List of expected main menu items
    items = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]

    # Validate each menu item
    for item in items:
        logger.info(f"Checking visibility of menu item: {item}")

        # Step 1: Ensure the menu item is visible
        assert db.is_visible(db.menu_item(item)), f"{item} menu item not visible on dashboard"
        logger.info(f"{item} menu item is visible")

        # Step 2: Try clicking the menu item
        db.open_menu(item)
        logger.info(f"Clicked on {item} menu item successfully")

    logger.info("Test test_main_menu_items_visible_clickable completed successfully")
