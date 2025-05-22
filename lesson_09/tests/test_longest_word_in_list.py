import pytest
from lesson_09.homeworks import longest_word_in_list

@pytest.mark.positive
@pytest.mark.parametrize("expected_value, test_data", [
    ('as df', ['', 'a', 'as df','as', 'asd'])
])
def test_longest_word_in_list_positive(expected_value, test_data):
    actual_value = longest_word_in_list(test_data)
    assert expected_value == actual_value, (f''
                                            f'Sum two value: expected value = {expected_value}, '
                                            f'but actual value = {actual_value}'
                                            )


@pytest.mark.negative
def test_longest_word_in_list_if_list_is_empty_negative():
    assert longest_word_in_list([]) == "Список порожній"


@pytest.mark.negative
@pytest.mark.parametrize("invalid_type_test_data", [
    (['', 'a', 'as df','as', 'asd', 0]),
    (['', 'a', 'as df','as', 'asd', None]),
    (['', 'a', 'as df','as', 'asd', True]),
    (['', 'a', 'as df','as', 'asd', False])
])
def test_longest_word_in_list_if_list_is_empty_negative(invalid_type_test_data):
    assert longest_word_in_list(invalid_type_test_data) == "Список містить не тільки строки"