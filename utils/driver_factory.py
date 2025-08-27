from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from utils import config

# ============================================================
# Driver Factory
# Creates a WebDriver instance based on the chosen browser.
# Supported browsers: Chrome, Firefox, Edge
# ============================================================

# Note: If webdriver_manager is not installed,
# ensure that the corresponding browser drivers
# (chromedriver, geckodriver, msedgedriver) are available in your PATH.

def get_driver(browser: str = None):
    """
    Returns a Selenium WebDriver instance for the given browser.
    
    Args:
        browser (str): Browser name ("chrome", "firefox", "edge").
                       Defaults to value in config.DEFAULT_BROWSER.
    
    Returns:
        WebDriver: Selenium WebDriver instance.
    """
    
    # Use the provided browser name or fallback to default from config
    browser = (browser or config.DEFAULT_BROWSER).lower()
    
    # ---------- Chrome ----------
    if browser == "chrome":
        opts = ChromeOptions()
        opts.add_argument("--start-maximized")  # open browser maximized
        return webdriver.Chrome(service=ChromeService(), options=opts)
    
    # ---------- Firefox ----------
    if browser == "firefox":
        opts = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(), options=opts)
        driver.maximize_window()  # maximize after start
        return driver
    
    # ---------- Edge ----------
    if browser == "edge":
        opts = EdgeOptions()
        return webdriver.Edge(service=EdgeService(), options=opts)
    
    # ---------- Default (Chrome) ----------
    # If an unknown browser is passed, fallback to Chrome
    opts = ChromeOptions()
    opts.add_argument("--start-maximized")
    return webdriver.Chrome(service=ChromeService(), options=opts)
