import logging
import pytest
from lesson_23.api_tests.get_cars_tests.get_cars_method import GetCars

logger = logging.getLogger(__name__)

def assert_sorted(values, key_name):
    for i in range(1, len(values)):
        assert values[i] >= values[i - 1], f"{key_name} not sorted: {values[i]} < {values[i-1]}"
        logger.info(f"{key_name}: {values[i-1]} <= {values[i]}")


@pytest.mark.parametrize(
    "value_sort_by, key, cast", [
    ("engine_volume", "engine_volume", float),
    ("price", "price", float),
    ("year", "year", int)
])
@pytest.mark.parametrize("limit", [2, 3, 5, 10])
def test_combo_sorting_numerical(auth_session, base_url, value_sort_by, key, cast, limit):
    api = GetCars(base_url, auth_session)
    response = api.get_cars(sort_by=value_sort_by, limit=limit)

    data = response.json()
    assert len(data) > 1, f'Response data has 0 or 1 object. Comparison is impossible'
    assert len(data) == limit, f"Response data returned incorrect limit: Response data={len(data)} but expected {limit}"


    values = [cast(car[key]) for car in data]
    assert_sorted(values, key)

def test_brand_sorted_alphabetically(auth_session, base_url):
    api = GetCars(base_url, auth_session)
    response = api.get_cars(sort_by='brand')

    data = response.json()
    brands = [car['brand'] for car in data]

    for i in range(1, len(brands)):
        assert brands[i - 1].lower() <= brands[i].lower(), (
            f"Brand not sorted correctly alphabetically: after '{brands[i-1]}' can't be '{brands[i]}'"
        )
        logger.info(f"Brand order OK: after {brands[i - 1]} should be {brands[i]}")


@pytest.mark.parametrize(
    'expected_limit_value',
    [1, 3, 5, 10, 15, 20, 25]
)
def test_cars_limit(base_url, auth_session, expected_limit_value):
    api = GetCars(base_url, auth_session)
    response = api.get_cars(limit=expected_limit_value)

    data = response.json()

    assert len(data) == expected_limit_value, f"Returned {len(data)} cars, expected limit {expected_limit_value}"

    logging.info(f"TEST PASSED for limit={expected_limit_value}, returned={len(data)}")


@pytest.mark.parametrize(
    ('expected_limit_value', 'test_limit_value'),[
    (25, 0)
    ]
)
def test_cars_with_null_limit(base_url, auth_session, expected_limit_value,test_limit_value):
    api = GetCars(base_url, auth_session)
    response = api.get_cars(limit=test_limit_value)

    data = response.json()

    assert len(data) == expected_limit_value, f"Expected all cars when limit=0, but received {len(data)}"
    logging.info(f"TEST PASSED for limit=0, returned {len(data)} cars (assumed all).")


@pytest.mark.parametrize([
    'expected_limit_value', 'test_limit_value'],[
    (25, 26)
])
def test_cars_limit_negative(base_url, auth_session, expected_limit_value, test_limit_value):
    api = GetCars(base_url, auth_session)
    response = api.get_cars(limit=test_limit_value)

    data = response.json()
    assert  len(data) == expected_limit_value, f"Returned more cars than ({len(data)}) than limit {expected_limit_value}"
    logging.info(f"TEST PASSED for limit_value={test_limit_value}, returned={len(data)}")




if __name__ == '__main__':
    pytest.main()
