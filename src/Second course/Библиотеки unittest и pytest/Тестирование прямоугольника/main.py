import pytest
from yandex_testing_lesson import Rectangle


def test_invalid_constructor_width():
    with pytest.raises(ValueError):
        Rectangle(-5, 10)


def test_invalid_constructor_height():
    with pytest.raises(ValueError):
        Rectangle(10, -5)


def test_valid_constructor():
    for i in range(1, 100):
        for j in range(1, 100):
            try:
                Rectangle(i, j)
            except ValueError:
                pytest.fail("Unexpected error")


def test_invalid_type():
    with pytest.raises(TypeError):
        Rectangle([], 5)


def test_invalid_type_2():
    with pytest.raises(TypeError):
        Rectangle(5, [])


def test_invalid_type_3():
    with pytest.raises(TypeError):
        Rectangle([], [])


def test_invalid_type_4():
    with pytest.raises(TypeError):
        Rectangle("hi", 4)


def test_rectangle():
    for w in range(1, 100):
        for h in range(1, 100):
            w, h = 5, 4
            rect = Rectangle(w, h)
            assert rect.get_area() == w * h
            assert rect.get_perimeter() == (w + h) * 2

