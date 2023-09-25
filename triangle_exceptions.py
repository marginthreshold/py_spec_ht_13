class TriangleException(Exception):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __str__(self):
        text = "The triangle can't be existed"
        text_less_then_zero = "Sides should be positive (greater than zero)."
        if self.side1 < 0 or self.side2 < 0 or self.side3 < 0:
            return text_less_then_zero
        elif self.side1 + self.side2 <= self.side3:
            return f"{text} \n" \
                   f"side1: {self.side1} + side2: {self.side2} not greater than side3: {self.side3}"
        elif self.side1 + self.side3 <= self.side2:
            return f"{text} \n" \
                   f"side1: {self.side1} + side3: {self.side3} not greater than side2: {self.side2}"
        elif self.side2 + self.side3 <= self.side1:
            return f"{text} \n" \
                   f"side2: {self.side2} + side3: {self.side3} not greater than side1: {self.side1}"
