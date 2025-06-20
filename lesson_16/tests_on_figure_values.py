import pytest
from lesson_16.homework_16_1_2 import Square, Rectangle, Circle, Triangle


@pytest.mark.positive
@pytest.mark.parametrize(
    "side_a, expected_area, expected_perimeter",
    [
        (2, 4, 8),
        (5, 25, 20)
    ]
)
def test_valid_area_and_perimeter_by_square(side_a, expected_area, expected_perimeter):
    actual_result = Square(side_a)
    assert actual_result.area() == expected_area
    assert actual_result.perimeter() == expected_perimeter


@pytest.mark.negative
@pytest.mark.parametrize(
    "invalid_side_a",
    [
        (-1, 0, "", [], {}, (), True, False)
    ]
)
def test_invalid_value_for_square(invalid_side_a):
    with pytest.raises((TypeError, ValueError)):
        Square(invalid_side_a)


@pytest.mark.positive
@pytest.mark.parametrize(
    "a, b, expected_area, expected_perimeter",
    [
        (3, 4, 12.0, 14.0),
        (5, 6, 30.0, 22.0)
    ]
)
def test_valid_area_and_perimeter_by_rectangle(a, b, expected_area, expected_perimeter):
    actual_result = Rectangle(a, b)
    assert actual_result.area() == expected_area
    assert actual_result.perimeter() == expected_perimeter


@pytest.mark.negative
@pytest.mark.parametrize("side_a, side_b",
    [
        (-2, 3),
        (2, -3),
        (2, 0),
        (0, 2),
        (3, '2'),
        ('2', 3),
        (4, False),
        (4, True),
        (True, 4),
        (False, 4),
    ]
)
def test_invalid_value_for_rectangle(side_a, side_b):
    with pytest.raises((ValueError, TypeError)):
        Rectangle(side_a, side_b)


@pytest.mark.positive
@pytest.mark.parametrize(
    "radius, expected_area, expected_perimeter",
    [
        (3, 28.274333882308138, 18.84955592153876)
    ]
)
def test_valid_area_and_perimeter_for_circle(radius, expected_area, expected_perimeter):
    actual_result = Circle(radius)
    assert actual_result.area() == expected_area
    assert actual_result.perimeter() == expected_perimeter


@pytest.mark.negative
@pytest.mark.parametrize(
    "radius", [0, -1, "", False, True, [], {}, ()])
def test_invalid_radius_for_circle(radius):
    with pytest.raises((ValueError, TypeError)):
        Circle(radius)



@pytest.mark.positive
@pytest.mark.parametrize(
    "a, b, c, expected_area, expected_perimeter",
    [(3, 4, 5, 6.0, 12.0), (6, 8, 10, 24.0, 24.0)]
)
def test_valid_triangle(a, b, c, expected_area, expected_perimeter):
    actual_result = Triangle(a, b, c)
    assert actual_result.area() == expected_area
    assert actual_result.perimeter() == expected_perimeter

@pytest.mark.negative
@pytest.mark.parametrize("a, b, c", [
    (-1, 2, 3),
    (4, -5, 6),
    (4, 5, -6),
    (3, 0, 3),
    (3, 4, ""),
    (1, 2, 3),
    (10, 1, 1),
    (True, 4, 5)
])
def test_invalid_side_value_for_triangle(a, b, c):
    with pytest.raises((ValueError, TypeError)):
        Triangle(a, b, c)
