import pytest
from existed_triangle import Triangle


def test_triangels():
    assert (Triangle(3, 3, 3).check_triangle() == 'This triangle is equilateral')
    assert (Triangle(3, 3, 4).check_triangle() == 'This triangle is isosceles')
    assert (Triangle(3, 4, 5).check_triangle() == 'This triangle is scalene')


if __name__ == '__main__':
    pytest.main()
