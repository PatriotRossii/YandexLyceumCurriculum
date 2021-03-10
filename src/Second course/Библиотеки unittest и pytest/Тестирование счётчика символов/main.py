import pytest
from yandex_testing_lesson import count_chars


def test_default():
    assert count_chars("hi") == {"h": 1, "i": 1}


def test_empty():
    assert count_chars("") == {}


def test_list_type():
    with pytest.raises(TypeError):
        reverse(["hi"])


def test_int_type():
    with pytest.raises(TypeError):
        reverse(1)


def test_dict_type():
    with pytest.raises(TypeError):
        reverse({"hi": 1})


def test_digits():
    assert count_chars("hello1231") == {
        "h": 1, "e": 1, "l": 2, "o": 1,
        "1": 2, "2": 1, "3": 1
    }