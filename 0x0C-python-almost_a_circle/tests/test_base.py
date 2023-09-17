import unittest
from models.base import Base


class MyTestCase(unittest.TestCase):
    def test_instance(self):
        instance = Base()
        self.assertIsInstance(instance, Base)

    def test_id_init(self):
        instance1 = Base()
        instance2 = Base(19)
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 19)

    def test_multiple_parameters(self):
        with self.assertRaises(TypeError):
            instance = Base(1, 19)
