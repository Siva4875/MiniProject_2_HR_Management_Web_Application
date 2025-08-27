import os
import sys
import pytest
import logging
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.driver_factory import get_driver

# Set up logger for this conftest
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Ensure project root is on sys.path so imports work correctly
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


def pytest_addoption(parser):
    """
    Register custom CLI options for pytest.
    Example usage:
        pytest --browser-name=firefox
    """
    parser.addoption(
        "--browser-name",
        action="store",
        default="chrome",
        help="Browser to run tests (chrome, firefox, chromium)",
    )


@pytest.fixture(scope="session")
def browser(request):
    """
    Fixture to fetch browser name from pytest command line.
    Defaults to 'chrome' if not provided.
    """
    browser_name = request.config.getoption("--browser-name")
    logger.info(f"Selected browser: {browser_name}")
    return browser_name


@pytest.fixture(scope="function")
def driver(browser):
    """
    Fixture to initialize and quit WebDriver for each test function.
    Ensures clean browser instance for every test.
    """
    logger.info(f"Launching WebDriver for browser: {browser}")
    driver = get_driver(browser)
    yield driver
    logger.info("Closing WebDriver instance.")
    driver.quit()


@pytest.fixture
def login_as_admin(browser):
    """
    Fixture to:
    1. Launch browser
    2. Navigate to login page
    3. Perform login with dummy admin credentials
    4. Return DashboardPage object
    Cleans up WebDriver after test.
    """
    logger.info("Launching browser and navigating to login page.")
    driver = get_driver(browser)

    login_page = LoginPage(driver)
    login_page.load()

    logger.info("Performing login as Admin.")
    login_page.do_login("Admin", "admin123")  # dummy credentials

    dashboard_page = DashboardPage(driver)

    logger.info("Admin successfully logged in, returning DashboardPage object.")
    yield dashboard_page

    logger.info("Closing WebDriver instance after test.")
    driver.quit()
