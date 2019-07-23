import pytest

def sum(a,b):
    return a+b

@pytest.mark.parametrize("input1, input2, output",
                         [
                             (2, 3, 5),
                             (5, 5, 10),
                             (3, 3, 8),
                             (10, 3, 12),
                             (5, 6, 10),
                             (3, 3, 8)
                         ]
                         )
def test_cal_sum_1(input1, input2, output):
    result = sum(input1 , input2)
    assert result == output
