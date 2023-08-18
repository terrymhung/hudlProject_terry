from tst_login import test_login_with_invalid_credentials
from tst_login import test_login_with_valid_credentials
from tst_login import test_login_with_no_credentials
from tst_login import test_login_only_username
from tst_login import clear_input_fields

# Test a failed login attempt.
test_login_with_invalid_credentials()
print("Attempt login with invalid credentials - Pass")
clear_input_fields()

# Test with only username.
test_login_only_username()
print("Attempt login with only user name - Pass")
clear_input_fields()

# Test with no credentials.
test_login_with_no_credentials()
print("Attempt login with no credentials - Pass")

# Test a successful login attempt.
test_login_with_valid_credentials()
print("Login with valid credentials - Pass")

