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
        if self.side1 == self.side2 == self.side3:
            print("This triangle is equilateral")
        elif self.side1 == self.side2 or \
                self.side1 == self.side3 or \
                self.side2 == self.side3:
            print("This triangle is isosceles")
        else:
            print("This triangle is scalene")


if __name__ == '__main__':
    triangle1 = Triangle(3, 4, 5)
    triangle1.check_triangle()
