import pytest
from trial4_first_assignment import dividenum

@pytest.mark.parametrize("x,y,result",
[(40,10,4),
(49,7,7),
pytest.param(90,10, 9, marks=pytest.mark.xfail)
]
                         )
def test_all(x,y,result):
    assert dividenum(x,y) == result
