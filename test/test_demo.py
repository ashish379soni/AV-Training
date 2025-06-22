"""Test using pytest"""
import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from area import circle
def test_area_of_circle():
    """Basic tests"""
    assert circle(5) == pytest.approx(78.54, rel=1e-2)
    assert circle(0) == 0
    assert circle(1) == pytest.approx(3.14, rel=1e-2)

