from tst_login import test_login_with_invalid_credentials
from tst_login import test_login_with_valid_credentials
from tst_login import test_login_with_no_credentials
from tst_login import test_login_only_username
from tst_login import clear_input_fields

# Test a failed login attempt.
test_login_with_invalid_credentials()
clear_input_fields()

# Test with only username.
test_login_only_username()
clear_input_fields()

# Test with no credentials.
test_login_with_no_credentials()

# Test a successful login attempt.
test_login_with_valid_credentials()

