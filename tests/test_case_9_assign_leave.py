import logging
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage

# Configure logger for this test module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test_assign_leave(login_as_admin):
    """
    Test Case:
    1. Login as admin (via fixture)
    2. Navigate to 'Leave' section
    3. Assign leave to a specific employee
    4. Verify that the leave assignment is successful
    """

    logger.info("Starting test: test_assign_leave")

    # Step 1: Get DashboardPage instance from fixture
    db: DashboardPage = login_as_admin
    logger.info("Logged in as Admin successfully")

    # Step 2: Navigate to "Leave" menu
    db.open_menu("Leave")
    logger.info("Navigated to 'Leave' section")

    # Step 3: Initialize LeavePage
    lp = LeavePage(db.driver)

    # Step 4: Assign leave to employee (change employee name if needed)
    employee_name = "Charles  Carter"
    logger.info(f"Attempting to assign leave to employee: {employee_name}")

    # Perform leave assignment and assert
    assert lp.assign_leave(employee_name, days=1), f"Leave assignment failed for {employee_name}"
    logger.info(f"Leave successfully assigned to employee: {employee_name}")

    logger.info("Test test_assign_leave completed successfully")
