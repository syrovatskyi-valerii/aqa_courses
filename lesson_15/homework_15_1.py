class Diamond:
    def __init__(self, side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a

    def __setattr__(self, key, value):

        if key == 'side_a' and value is None:
            raise ValueError("Сторона \"А\" не може бути None")

        if key == 'side_a' and type(value) not in (int, float):
            raise ValueError("Сторона \"А\" повинна бути int або float")

        if key == 'side_a' and value <= 0:
            raise ValueError("Сторона \"А\" повинна бути більшою за 0.")

        if key == 'corner_a' and value is None:
            raise ValueError("Кут \"А\" не може бути None")

        if key == 'corner_a' and type(value) not in (int, float):
            raise ValueError("Кут \"А\" повинен бути int або float")

        if key == 'corner_a' and not (0 < value < 180):
            raise ValueError("Кут \"А\" повинен бути між 0 і 180 градусів (не включно).")
        super().__setattr__('corner_b', 180 - value)

        if key == 'corner_b' and not (0 < value < 180):
            raise ValueError("Кут \"B\" повинен бути між 0 і 180 градусів (не включно).")

        super().__setattr__(key, value)


    def __str__(self):
        return f"Diamond: side_a = {self.side_a}, corner_a = {self.corner_a}, corner_b = {self.corner_b}"
