OrangeHRM Selenium-PyTest Automation

Project Overview:

- This project automates the testing of the HR management web application OrangeHRM Demo.
- The automation framework validates critical workflows like login, user management, menu navigation, leave assignment, and claims   handling.
- The framework is designed with Page Object Model (POM), PyTest, Selenium, and Allure reporting, ensuring test reusability, maintainability, and reliability.

Objectives:

- Automate end-to-end testing of key OrangeHRM modules.
- Validate core functionalities like login, logout, user creation, leave assignment, and claims.
- Support cross-browser execution (Chrome, Firefox, Edge).
- Generate structured logs and Allure HTML reports for test analysis.

Test Scenarios Covered:

- Login with multiple credentials (valid & invalid).
- Validate accessibility of home URL.
- Verify login page fields.
- Check visibility of main menu items post-login.
- Create new user and validate login.
- Search newly created user in Admin list.
- Test Forgot Password functionality.
- Verify My Info sub-menu items.
- Assign leave and validate records.
- Submit a claim request and verify history.

Setup & Execution:
Prerequisites:

- Python 3.8+
- Google Chrome / Firefox / Edge

Install dependencies:

    pip install -r requirements.txt

Run Tests:
    
    pytest --browser=chrome --alluredir=reports/allure-results

View Allure Report
    allure serve reports/allure-results

Best Practices Implemented

- Page Object Model (POM) for maintainability.
- Explicit waits for reliable element interaction.
- Logging (console + file).
- Exception handling for test resilience.
- Cross-browser compatibility.


Allure report integration:

    pytest -v --browser-name=chromium --alluredir=reports/allure-results


Specific tests:

    pytest tests/test_case_1_login_ddt.py


Open Allure report:

    allure serve reports/allure-results


Notes:
- Locators target the current OrangeHRM demo (v5 UI). Minor UI changes may require locator updates.
- New user creation uses existing employee "Charles  Carter" and role "ESS" with "Enabled" status.
- CSV files follow your sample header structure and include an additional 'Expected' column where needed.
- Tests use explicit waits and basic exception handling; logs are stored under 'reports/run.log'.
- The suite logs in/out cleanly and quits the browser after each test via fixtures.
- Under the 'data' file of 'new_user_data.csv' file change the NewUsername column value if required.
- In 'test_case_9_assign_leave.py' file under Step 4: Assign leave to employee (change employee name if needed).
