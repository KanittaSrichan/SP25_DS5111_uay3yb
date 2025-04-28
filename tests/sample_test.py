import pytest
import sys
sys.path.append('.')

import bin.sample_adder as adder

@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (1, 4, 5), (0, 0, 0), (10, 20, 30)])
def test_adder(a, b, expected):
    result = adder.add(a, b)
    assert result == expected, f"Adder failed with {a} + {b}, expected {expected}, got {result}"
