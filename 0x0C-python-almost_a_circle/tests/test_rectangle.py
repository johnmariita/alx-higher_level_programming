import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_instance(self):
        rect = Rectangle(1, 2)
        self.assertIsInstance(rect, Rectangle)

    def test_id_init(self):
        rect1 = Rectangle(1, 2)
        x = rect1.id
        rect2 = Rectangle(1, 2, id=19)
        self.assertEqual(rect1.id, x)
        self.assertEqual(rect2.id, 19)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            rect3 = Rectangle()

    def test_neg_width1(self):
        with self.assertRaises(ValueError):
            rect4 = Rectangle(-1, 1)

    def test_neg_width2(self):
        with self.assertRaises(ValueError):
            rect5 = Rectangle(-1, -1)

    def test_width_zero1(self):
        with self.assertRaises(ValueError):
            rect6 = Rectangle(0, 1)

    def test_width_zero2(self):
        with self.assertRaises(ValueError):
            rect7 = Rectangle(0, 1)

    def test_height_zero1(self):
        with self.assertRaises(ValueError):
            rect8 = Rectangle(1, 0)

    def test_height_zero2(self):
        with self.assertRaises(ValueError):
            rect9 = Rectangle(1, 0)

    def test_diff_type1(self):
        with self.assertRaises(TypeError):
            rect10 = Rectangle("19", 1)

    def test_diff_type2(self):
        with self.assertRaises(TypeError):
            rect11 = Rectangle(19, "1")

    def test_negX(self):
        with self.assertRaises(ValueError):
            rect12 = Rectangle(19, 19, x=-2)

    def test_negY(self):
        with self.assertRaises(ValueError):
            rect13 = Rectangle(19, 19, y=-2)

# The setters

    def test_width_setter(self):
        rect14 = Rectangle(2, 2)
        rect14.width = 19
        self.assertEqual(rect14.width, 19)

    def test_width_setter_negValue(self):
        rect15 = Rectangle(2, 2)
        with self.assertRaises(ValueError):
            rect15.width = -1

    def test_width_setter_nonInt(self):
        rect16 = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            rect16.width = "John"

    def test_width_setter_zero(self):
        rect = Rectangle(2, 2)
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_height_setter(self):
        rect = Rectangle(2, 2)
        rect.height = 19
        self.assertEqual(rect.height, 19)

    def test_height_setter_negValue(self):
        rect = Rectangle(2, 2)
        with self.assertRaises(ValueError):
            rect.height = -1

    def test_height_setter_nonInt(self):
        rect = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            rect.height = "John"

    def test_height_setter_zero(self):
        rect = Rectangle(2, 2)
        with self.assertRaises(ValueError):
            rect.height = 0

# Arguments received
    def test_no_positional_args(self):
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_one_positional_arg(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(19)

    def test_unknown_kwarg(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 2, z=19)

# The getters

    def test_width_getter(self):
        rect = Rectangle(2, 2)
        width = rect.width
        self.assertEqual(width, 2)

    def test_height_getter(self):
        rect = Rectangle(2, 2)
        height = rect.height
        self.assertEqual(height, 2)

    def test_x_getter(self):
        rect = Rectangle(2, 2)
        x = rect.x
        self.assertEqual(x, 0)

    def test_y_getter(self):
        rect = Rectangle(2, 2)
        y = rect.y
        self.assertEqual(y, 0)

    def test_area_method(self):
        rect = Rectangle(2, 2)
        area = rect.area()
        self.assertEqual(area, 4)
