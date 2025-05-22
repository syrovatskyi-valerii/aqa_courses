import pytest
import itertools

from lesson_09.homeworks import count_sum

@pytest.mark.positive
@pytest.mark.parametrize("a, b, expected_value", [
    (2, 2, 4),
    (3, 5, 8),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_sum_two_values_positive(a, b, expected_value):
    actual_value = count_sum(a, b)
    assert expected_value == actual_value, (f''
                                            f'Sum two value: expected value = {expected_value}, '
                                            f'but actual value = {actual_value}'
                                            )


invalid_values = [True, False, None, 'string', [], {}, (), set(), object()]
@pytest.mark.negative
@pytest.mark.parametrize("invalid_type_a, invalid_type_b",
        [(a, b) for a, b in itertools.product(invalid_values, repeat=2)
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float))
])
def test_sum_two_values_negative(invalid_type_a, invalid_type_b):
    assert count_sum(invalid_type_a, invalid_type_b) == "Увага: аргументи мають бути числами"
