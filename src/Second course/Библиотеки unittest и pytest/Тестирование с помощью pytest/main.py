import pytest
from yandex_testing_lesson import reverse


def test_empty():
    assert reverse('') == ''


def test_list_type():
    with pytest.raises(TypeError):
        reverse(["hi"])


def test_int_type():
    with pytest.raises(TypeError):
        reverse(1)


def test_dict_type():
    with pytest.raises(TypeError):
        reverse({"h": 1})


def test_palindrome():
    assert reverse("hih") == "hih"


def test_one_letter():
    assert reverse("a") == "a"


def test_default():
    assert reverse("hello, friend") == "dneirf ,olleh"
