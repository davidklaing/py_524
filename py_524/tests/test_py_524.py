import pytest
from py_524 import utils

def test_standard_deviation():
    assert standard_deviation([1,1,1]) == 0, 'standard deviation of [1,1,1] should equal 0'
