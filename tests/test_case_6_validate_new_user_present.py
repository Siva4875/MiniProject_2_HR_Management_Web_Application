import csv
import logging
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

# Configure logger for this test file
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def read_user():
    """
    Utility function to read the first row of user data
    from the CSV file `data/new_user_data.csv`.
    """
    logger.info("Reading user data from CSV file: data/new_user_data.csv")
    with open("data/new_user_data.csv", newline="") as f:
        data = list(csv.DictReader(f))[0]
        logger.info(f"User data loaded for validation: Username={data['NewUsername']}")
        return data


def test_new_user_present(login_as_admin):
    """
    Test Case:
    1. Login as Admin (fixture: login_as_admin)
    2. Navigate to Admin Page
    3. Search for the newly created user
    4. Assert that the user is found in listing
    """

    logger.info("Starting test: test_new_user_present")

    # Step 1: Admin dashboard page from fixture
    db: DashboardPage = login_as_admin
    logger.info("Admin login successful, DashboardPage loaded")

    # Step 2: Load test user data
    data = read_user()

    # Step 3: Navigate to Admin Page
    db.open_menu("Admin")
    logger.info("Navigated to Admin Page")

    # Step 4: Search for the user in listing
    ap = AdminPage(db.driver)
    logger.info(f"Searching for new user: {data['NewUsername']}")
    found = ap.search_user(data["NewUsername"])

    # Step 5: Verify user presence
    assert found, f"New user '{data['NewUsername']}' not found in listing"
    logger.info(f"New user '{data['NewUsername']}' found in listing")

    logger.info("Test test_new_user_present completed successfully")
