from tst_login import test_login_with_invalid_credentials
from tst_login import test_login_with_valid_credentials
from tst_login import create_account
from tst_login import forgot_password

# Test a failed login attempt.
test_login_with_invalid_credentials()

# Test the forgot password link
forgot_password()

# Test the create account link
create_account()

# Test a successful login attempt.
test_login_with_valid_credentials()
