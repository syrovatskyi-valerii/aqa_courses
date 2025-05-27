import pytest
from lesson_10.homework_10 import log_event
from lesson_10.def_for_logs import  read_last_n_log_levels
from lesson_10.def_for_logs import  clear_log_file

clear_log_file()

@pytest.mark.parametrize("username,expected_status,expected_level", [
    ("test_user_1", "success", "INFO"),
    ("test_user_2", "expired", "WARNING"),
    ("test_user_3", "failed", "ERROR")
])
def test_login_events(username, expected_status, expected_level):
    log_event(username=username, status=expected_status)
    levels = read_last_n_log_levels("login_system.log")
    actual_level = levels[-1]
    assert actual_level == expected_level
