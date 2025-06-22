import pytest
from area import circle

def test_area_of_circle():
    assert circle(5) == pytest.approx(78.54, rel=1e-2)
    assert circle(0) == 0
    assert circle(1) == pytest.approx(3.14, rel=1e-2)

