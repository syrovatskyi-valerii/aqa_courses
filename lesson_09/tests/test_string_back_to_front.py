import pytest

from lesson_09.homeworks import string_back_to_front

@pytest.mark.positive
@pytest.mark.parametrize("expected_value, test_data", [
    ('Hillel', 'lelliH'),
    ('0987654321', '1234567890')
])
def test_string_back_to_front_positive(expected_value, test_data):
    actual_value = string_back_to_front(test_data)
    assert expected_value == actual_value, (f''
                                            f'Sum two value: expected value = {expected_value}, '
                                            f'but actual value = {actual_value}'
                                            )


@pytest.mark.negative
@pytest.mark.parametrize("invalid_type_test_data", [
    ([1, True, False, None])
])
def test_string_back_to_front_negative(invalid_type_test_data):
    assert string_back_to_front(invalid_type_test_data) == "Увага: аргумент мають бути рядком"