import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = "https://identity.hudl.com/login?state=hKFo2SBhcXY1NXdscXZLTUxRbU5WcldLeEVZU3JEWWhTM0gyRqFupWxvZ2luo3RpZNkgZFRURVZOQ3NTNE9SM0hoVnRveDVSUkt6b1AwUlBHZGmjY2lk2SBuMTNSZmtIektvemFOeFdDNWRaUW9iZVdHZjRXalNuNQ&client=n13RfkHzKozaNxWC5dZQobeWGf4WjSn5&protocol=oauth2&response_type=id_token&redirect_uri=https%3A%2F%2Fwww.hudl.com%2Fapp%2Fusers%2Foidc%2Fcallback&scope=openid%20profile%20email&nonce=YtQk5eC%2FkqsZ87kIIIq5LgHoS%2BqSMJQaGkd%2BNtxDWYA%3D&response_mode=form_post&screen_hint="
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the Hudl login page and maximize window.
driver.get(url)
driver.maximize_window()

def forgot_password():
    """
    Logs in to the Hudl forgot password page.
    """

    # Click the Forgot Password link.
    forgot_password_link = driver.find_element("id", "forgot-password")
    forgot_password_link.click()

    # Wait for the Forgot Password page to load.
    time.sleep(2)

    # Verify that the Forgot Password page was opened.
    if driver.title == "Forgot Password":
        print("[+] Forgot Password page opened")
        # Navigate back to log in page
        forget_back_to_login = driver.find_element(By.CLASS_NAME,"uni-button--minimal")
        forget_back_to_login.click()
    else:
        print("[-] Forgot Password link failed")

def create_acccount():
    """
    Opens the create account page.
    """

    # Click the Create Account link.
    create_account_link = driver.find_element(By.ID, "btn-show-signup")
    create_account_link.click()

    # Wait for the create account page to load.
    time.sleep(2)

    # Verify that the create account page was opened.
    if driver.title == "Sign Up":
        print("[+] Create Account page opened")
        # Navigate back to log in page
        create_back_to_login = driver.find_element(By.CLASS_NAME, "uni-button--minimal")
        create_back_to_login.click()
    else:
        print("[-] Create Account link failed")

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
def test_login_with_valid_credentials():
    """
    Tests the login process with valid credentials.
    """
    username = "terrymhung@gmail.com"
    password = "pass4Hudl"

    login_with_credentials(username, password)

if __name__ == "__main__":

    # Test a failed login attempt.
    test_login_with_invalid_credentials()

    # Test the forgot password link
    forgot_password()

    # Test the create account link
    create_acccount()

    # Test a successful login attempt.
    test_login_with_valid_credentials()

    driver.quit()