import csv
import logging
import time
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.login_page import LoginPage

# Configure logger for this test file
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def read_user():
    """
    Utility function to read the first row of user data
    from the CSV file `data/new_user_data.csv`.
    """
    logger.info("Reading new user test data from CSV file")
    with open("data/new_user_data.csv", newline="") as f:
        data = list(csv.DictReader(f))[0]
        logger.info(f"User data loaded: Employee={data['EmployeeName']}, Username={data['NewUsername']}")
        return data


def test_create_user_and_login(login_as_admin):
    """
    Regression Test:
    1. Login as Admin
    2. Navigate to Admin Page
    3. Create a new user with given test data
    4. Logout as Admin
    5. Login with the newly created user credentials
    6. Validate successful login
    """

    logger.info("Starting test: test_create_user_and_login")

    # Step 1: Admin already logged in from fixture
    db: DashboardPage = login_as_admin
    logger.info("Admin login successful, DashboardPage loaded")

    # Step 2: Navigate to Admin Page
    db.open_menu("Admin")
    logger.info("Navigated to Admin Page")
    ap = AdminPage(db.driver)

    # Step 3: Create a new user using test data
    data = read_user()
    logger.info(f"Attempting to create new user: {data['NewUsername']}")
    created = ap.add_user(
        employee=data["EmployeeName"],
        new_username=data["NewUsername"],
        pwd=data["Password"]
    )

    assert created, "Failed to create user"
    logger.info(f"User '{data['NewUsername']}' created successfully")

    # Step 4: Logout as Admin
    db.logout()
    logger.info("Admin logged out successfully")

    # Step 5: Attempt login with new user credentials
    lp = LoginPage(db.driver)
    logger.info(f"Logging in with new user: {data['NewUsername']}")
    lp.do_login(data["NewUsername"], data["Password"])

    # Step 6: Verify successful login for new user
    assert DashboardPage(db.driver).is_logged_in(), "New user unable to login"
    logger.info(f"New user '{data['NewUsername']}' logged in successfully")

    logger.info("Test test_create_user_and_login completed successfully")
