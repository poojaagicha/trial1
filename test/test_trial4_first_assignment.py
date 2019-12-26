import pytest
from trial4_first_assignment import dividenum, multiplynum

@pytest.mark.parametrize("x,y,result",
[(40,10,4),
(49,7,7),
pytest.param(90,10, 9, marks=pytest.mark.xfail)
]
                         )
def test_divide(x,y,result):
    assert dividenum(x,y) == result

@pytest.mark.parametrize("x,y,expected",
[(20,10,200),
 (5,8,40),
pytest.param(90,10, 110, marks=pytest.mark.xfail)
 ]
                        )
def test_multiply(x,y,expected):
    assert multiplynum(x,y) == expected

