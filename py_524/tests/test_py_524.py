import pytest
from py_524 import utils

class Test_standard_deviation:

    def test_math(self):
        assert utils.standard_deviation([1,1,1]) == 0, 'standard deviation of [1,1,1] should equal 0'
