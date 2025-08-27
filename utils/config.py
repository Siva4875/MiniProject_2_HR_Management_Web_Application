import os

# ==============================
# Global configuration settings
# ==============================

# Base URL of the OrangeHRM application.
# Can be overridden by setting the environment variable ORANGEHRM_URL.
BASE_URL = os.getenv("ORANGEHRM_URL", "https://opensource-demo.orangehrmlive.com/")

# Default login username for OrangeHRM.
# Can be overridden by setting the environment variable ORANGEHRM_USER.
DEFAULT_USER = os.getenv("ORANGEHRM_USER", "Admin")

# Default login password for OrangeHRM.
# Can be overridden by setting the environment variable ORANGEHRM_PASS.
DEFAULT_PASS = os.getenv("ORANGEHRM_PASS", "admin123")

# Default browser to use for tests.
# Supported values: chrome | firefox | edge.
# Can be overridden by setting the environment variable BROWSER.
DEFAULT_BROWSER = os.getenv("BROWSER", "chrome")

# Explicit wait time (in seconds) for Selenium WebDriver.
# Used to wait for elements to become visible/clickable.
# Can be overridden by setting the environment variable EXPLICIT_WAIT.
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "12"))
