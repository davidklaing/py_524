import pytest

from py_524 import utils


def test_sd_math():
    assert utils.standard_deviation([0, 1]) == 0.7071067811865476


def test_sd_at_least_length_three():
    assert utils.standard_deviation([0, 1, 2]) == 1


def test_sd_neg_numbers():
    assert utils.standard_deviation([-1, 0, 1]) == 1


def test_sd_same_element():
    assert utils.standard_deviation([100, 100, 100]) == 0


def test_sd_too_small():
    with pytest.raises(ZeroDivisionError):
        utils.standard_deviation([0])


def test_sd_is_list():
    with pytest.raises(TypeError):
        utils.standard_deviation(0)


def test_sd_null():
    with pytest.raises(TypeError):
        utils.standard_deviation()


def test_sd_string_convert():
    with pytest.raises(TypeError):
        utils.standard_deviation(["0", "1"])


def test_se_math():
    assert utils.standard_error([0, 1]) == 0.5


def test_se_at_least_length_three():
    assert utils.standard_error([0, 1, 2]) == 0.5773502691896258


def test_se_neg_numbers():
    assert utils.standard_error([-1, 0, 1]) == 0.5773502691896258


def test_se_same_element():
    assert utils.standard_error([100, 100, 100]) == 0


def test_se_too_small():
    with pytest.raises(ZeroDivisionError):
        utils.standard_error([0])


def test_se_is_list():
    with pytest.raises(TypeError):
        utils.standard_error(0)


def test_se_null():
    with pytest.raises(TypeError):
        utils.standard_error()


def test_se_string_convert():
    with pytest.raises(TypeError):
        utils.standard_error(["0", "1"])
