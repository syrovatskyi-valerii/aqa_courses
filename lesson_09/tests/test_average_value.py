import pytest

from lesson_09.homeworks import average_value

@pytest.mark.positive
@pytest.mark.parametrize("expected_value, test_data", [
    (4.5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (0,[0]),
    (-16,[-1, -2, -45]),
    (4.7, [2.5, 4.6, 6.99]),
    (101,[101])
])
def test_average_value_positive(expected_value, test_data):
    actual_value = average_value(test_data)
    assert expected_value == actual_value, (f''
                                            f'Sum two value: expected value = {expected_value}, '
                                            f'but actual value = {actual_value}'
                                            )


@pytest.mark.positive
def test_average_value_single_element_positive():
    assert average_value([42]) == 42.00


@pytest.mark.negative
@pytest.mark.parametrize("invalid_test_data", [
    ['1', 2, 3],
    [1, True, 3],
    [None, 5],
    [[1, 2], 3],
    [{"a": 1}, 3],
])
def test_average_value_with_invalid_types_negative(invalid_test_data):
    assert average_value(invalid_test_data) == "У списку мають бути лише числа"
