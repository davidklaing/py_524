import pytest
from py_524 import utils

class Test_standard_deviation:

    def test_math(self):
        assert utils.standard_deviation([0,1]) == 0.7071067811865476

    def test_atleast_length_three(self):
        assert utils.standard_deviation([0,1,2]) == 1

    def test_neg_numbers(self):
        assert utils.standard_deviation([-1, 0, 1]) == 1

    def test_same_element(self):
        assert utils.standard_deviation([100,100,100]) == 0

    def test_too_small(self):
        with pytest.raises(ZeroDivisionError):
            utils.standard_deviation([0])

    def test_is_list(self):
        with pytest.raises(TypeError):
            utils.standard_deviation(0)

    def test_null(self):
        with pytest.raises(TypeError):
            utils.standard_deviation()

    def test_string_convert(self):
        with pytest.raises(TypeError):
            utils.standard_deviation(["0", "1"])

class Test_standard_error:

    def test_math(self):
        assert utils.standard_error([0,1]) == 0.5

    def test_atleast_length_three(self):
        assert utils.standard_error([0,1,2]) == 0.5773502691896258

    def test_neg_numbers(self):
        assert utils.standard_error([-1, 0, 1]) == 0.5773502691896258

    def test_same_element(self):
        assert utils.standard_error([100,100,100]) == 0

    def test_too_small(self):
        with pytest.raises(ZeroDivisionError):
            utils.standard_error([0])

    def test_is_list(self):
        with pytest.raises(TypeError):
            utils.standard_error(0)

    def test_null(self):
        with pytest.raises(TypeError):
            utils.standard_error()

    def test_string_convert(self):
        with pytest.raises(TypeError):
            utils.standard_error(["0", "1"])
