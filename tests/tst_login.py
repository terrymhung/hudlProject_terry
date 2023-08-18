import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.hudl.com/login?utm_content=hudl_primary&utm_source=www.hudl.com&utm_medium=login_dropdown&utm_campaign=platform_logins"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the Hudl login page and maximize window.
driver.get(url)
driver.maximize_window()


def clear_input_fields():
    """
    Clears all input fields in the specified web driver.
    """

    # Get email field.
    username_input_fields = driver.find_elements(By.ID, "email")

    # Clear username field.
    for input_field in username_input_fields:
        if input_field.is_enabled():
            input_field.clear()

    # Get Password field
    password_input_fields = driver.find_elements(By.ID, "password")

    # Clear password field.
    for input_field in password_input_fields:
        if input_field.is_enabled():
            input_field.clear()

    time.sleep(4)


def login_with_credentials(username, password):
    """
    Logs in to the Hudl website with the specified credentials.

    Args:
        username: The username.
        password: The password.
    """
    # Enter the username and password.
    uname = driver.find_element(By.ID, "email")
    uname.send_keys(username)

    pword = driver.find_element(By.ID, "password")
    pword.send_keys(password)

    # Click the login button.
    driver.find_element(By.ID, "logIn").click()

    # Wait for the login process to complete.
    time.sleep(3)

    # Verify that the login was successful.
    error_message = "We don't recognize that email and/or password"
    errors = driver.find_elements(By.ID, "login-box")

    if any(error_message in e.text for e in errors):
        print("[-] Login unsuccessful")
    else:
        print("[+] Login successful")


def test_login_with_invalid_credentials():
    """
    Tests the login process with invalid credentials.
    """
    username = "terrymhung@gmail.com"
    password = "invalid_password"

    login_with_credentials(username, password)


def test_login_only_username():
    """
    Tests the login process with invalid credentials.
    """
    username = "terrymhung@gmail.com"
    password = ""

    login_with_credentials(username, password)


def test_login_with_no_credentials():
    """
    Tests the login process with invalid credentials.
    """
    username = ""
    password = ""

    login_with_credentials(username, password)


def test_login_with_valid_credentials():
    """
    Tests the login process with valid credentials.
    """
    username = "terrymhung@gmail.com"
    password = "pass4Hudl"

    login_with_credentials(username, password)

    # Close Chrome browser
    driver.quit()
