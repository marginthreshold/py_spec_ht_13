import io
import unittest
from unittest.mock import patch

from existed_triangle import Triangle


class TestTriangle(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_triangle_equilateral(self, mock_stdout):
        self.assertEqual(Triangle(3, 3, 3).check_triangle(), 'This triangle is equilateral')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_triangle_isosceles(self, mock_stdout):
        self.assertEqual(Triangle(3, 3, 4).check_triangle(), 'This triangle is isosceles')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_triangle_scalene(self, mock_stdout):
        self.assertEqual(Triangle(3, 4, 5).check_triangle(), 'This triangle is scalene')


if __name__ == '__main__':
    unittest.main(verbosity=2)
