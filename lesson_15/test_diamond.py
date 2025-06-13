import pytest
from lesson_15.homework_15_1 import Diamond


@pytest.mark.positive
@pytest.mark.parametrize(
    "side_a, corner_a, expected_corner_b",
    [
        (10, 60, 120),
        (5, 90, 90),
        (7.5, 40.5, 139.5),
    ]
)
def test_valid_diamond(side_a, corner_a, expected_corner_b):
    d = Diamond(side_a, corner_a)
    assert d.side_a == side_a
    assert d.corner_a == corner_a
    assert d.corner_b == expected_corner_b



@pytest.mark.negative
@pytest.mark.parametrize(
    "side_a, corner_a",
    [
        (0, 60),
        (-1, 90),
    ]
)
def test_invalid_side_a(side_a, corner_a):
    with pytest.raises(ValueError, match="Сторона \"А\" повинна бути більшою за 0."):
        Diamond(side_a, corner_a)



@pytest.mark.negative
@pytest.mark.parametrize(
    "side_a, corner_a",
    [
        (10, 0),
        (10, -1),
        (10, 180)
    ]
)
def test_invalid_corner_a(side_a, corner_a):
    with pytest.raises(ValueError, match="Кут \"А\" повинен бути між 0 і 180 градусів"):
        Diamond(side_a, corner_a)



@pytest.mark.negative
@pytest.mark.parametrize(
    "side_a, corner_a",
    [
        ('10', 90),
        (True, 90),
        (False, 90),
        ([], 90),
        ({}, 90),
        ((), 90)
    ]
)
def test_invalid_type_side_a(side_a, corner_a):
    with pytest.raises(ValueError, match="Сторона \"А\" повинна бути int або float"):
        Diamond(side_a, corner_a)



@pytest.mark.negative
@pytest.mark.parametrize(
    "side_a, corner_a",
    [
        (10 ,'10'),
        (10, True),
        (10, False),
        (10, []),
        (10, {}),
        (10, ())
    ]
)
def test_invalid_type_corner_a(side_a, corner_a):
    with pytest.raises(ValueError, match="Кут \"А\" повинен бути int або float"):
        Diamond(side_a, corner_a)



@pytest.mark.negative
@pytest.mark.parametrize(
    "side_a, corner_a",
    [
        (None ,10)
    ]
)
def test_side_a_could_not_be_none(side_a, corner_a):
    with pytest.raises(ValueError, match="Сторона \"А\" не може бути None"):
        Diamond(side_a, corner_a)



@pytest.mark.negative
@pytest.mark.parametrize(
    "side_a, corner_a",
    [
        (10, None)
    ]
)
def test_corner_a_could_not_be_none(side_a, corner_a):
    with pytest.raises(ValueError, match="Кут \"А\" не може бути None"):
        Diamond(side_a, corner_a)