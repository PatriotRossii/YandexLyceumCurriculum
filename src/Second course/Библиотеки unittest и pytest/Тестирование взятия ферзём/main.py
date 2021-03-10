import pytest
from yandex_testing_lesson import is_under_queen_attack

func = is_under_queen_attack

valid_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
valid_rows = ["1", "2", "3", "4", "5", "6", "7", "8"]


def test_invalid_position_1():
    with pytest.raises(TypeError):
        is_under_queen_attack(1, "e5")


def test_invalid_position_2():
    with pytest.raises(TypeError):
        is_under_queen_attack(["hi"], "e5")


def test_invalid_position_3():
    with pytest.raises(TypeError):
        is_under_queen_attack({"hi": 1}, "e5")


def test_invalid_position_4():
    with pytest.raises(TypeError):
        is_under_queen_attack("e5", 1)


def test_invalid_position_5():
    with pytest.raises(TypeError):
        is_under_queen_attack("e5", ["hi"])


def test_invalid_position_6():
    with pytest.raises(TypeError):
        is_under_queen_attack("e5", {"hi": 1})


def test_invalid_coordinate_1():
    with pytest.raises(ValueError):
        is_under_queen_attack("abc", "e5")


def test_invalid_coordinate_2():
    with pytest.raises(ValueError):
        is_under_queen_attack("", "e5")


def test_invalid_coordinate_3():
    with pytest.raises(ValueError):
        is_under_queen_attack("h0", "e5")


def test_invalid_coordinate_4():
    with pytest.raises(ValueError):
        is_under_queen_attack("abc", "e5")


def test_invalid_coordinate_5():
    with pytest.raises(ValueError):
        is_under_queen_attack("e5", "")


def test_invalid_coordinate_6():
    with pytest.raises(ValueError):
        is_under_queen_attack("e5", "h0")


def test_valid_coordinates():
    for column in valid_columns:
        for row in valid_rows:
            try:
                is_under_queen_attack(column + row, column + row)
            except RuntimeError:
                pytest.fail("Unexpected error")


def test_result():
    for x1 in range(1, 8):
        for y1 in range(1, 8):
            for x2 in range(1, 8):
                for y2 in range(1, 8):
                    qp = valid_columns[x1 - 1] + valid_rows[y1 - 1]
                    p = valid_columns[x2 - 1] + valid_rows[y2 - 1]
                    assert func(p, qp) == (y1 == y2 or x1 == x2 or (abs(x1 - x2) == abs(y1 - y2)))
