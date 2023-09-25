from triangle_exceptions import TriangleException


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        if self.side1 + self.side2 <= self.side3 or \
                self.side1 + self.side3 <= self.side2 or \
                self.side2 + self.side3 <= self.side1:
            raise TriangleException(self.side1, self.side2, self.side3)

    def check_triangle(self):
        """
        Check the kind of triangle.
        >>> triangle1=Triangle(3, 3, 3)
        >>> triangle1.check_triangle()
        'This triangle is equilateral'

        >>> triangle2=Triangle(3, 3, 4)
        >>> triangle2.check_triangle()
        'This triangle is isosceles'

        >>> triangle3=Triangle(3, 4, 5)
        >>> triangle3.check_triangle()
        'This triangle is scalene'

        """

        if self.side1 == self.side2 == self.side3:
            return "This triangle is equilateral"
        elif self.side1 == self.side2 or \
                self.side1 == self.side3 or \
                self.side2 == self.side3:
            return "This triangle is isosceles"
        else:
            return "This triangle is scalene"


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
    
