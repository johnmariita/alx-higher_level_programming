import unittest
from models.square import Square


class TestcaseSquare(unittest.TestCase):
    def test_insance(self):
        square = Square(19)
        self.assertIsInstance(square, Square)

    def test_id(self):
        square = Square(19, id = 1)
        self.assertEqual(square.id, 1)

    def test_size_getter(self):
        square = Square(19)
        x = square.size
        self.assertEqual(x, 19)

    def test_size_setter(self):
        square = Square(19)
        square.size = 1
        self.assertEqual(square.size, 1)

    def test_size_set_zero(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_size_set_zero2(self):
        square = Square(19)
        with self.assertRaises(ValueError):
            square.size = 0

    def test_size_set_negSize(self):
        with self.assertRaises(ValueError):
            square = Square(-1)

    def test_size_set_negSize2(self):
        square = Square(19)
        with self.assertRaises(ValueError):
            square.size = -1

    def test_size_set_nonInt_type(self):
        with self.assertRaises(TypeError):
            square = Square("John")

    def test_size_set_nonInt_type2(self):
        square = Square(19)
        with self.assertRaises(TypeError):
            square.size = "John"

    def test_positional_arg(self):
        with self.assertRaises(TypeError):
            square = Square()

    def test_area(self):
        square = Square(19)
        self.assertEqual(square.area(), 361)


