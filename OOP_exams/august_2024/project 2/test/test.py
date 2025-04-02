from project.furniture import Furniture
from typing import Tuple, Optional

import unittest


class TestFurniture(unittest.TestCase):

    # -- Construction and Default Values --

    def test_valid_creation(self):
        f = Furniture("Chair", 100.0, (50, 60, 70), in_stock=True, weight=20.0)
        self.assertEqual(f.model, "Chair")
        self.assertEqual(f.price, 100.0)
        self.assertEqual(f.dimensions, (50, 60, 70))
        self.assertTrue(f.in_stock)
        self.assertEqual(f.weight, 20.0)

    def test_default_values(self):
        f = Furniture("Table", 200.0, (100, 50, 75))
        self.assertTrue(f.in_stock)
        self.assertIsNone(f.weight)

    # -- Model Property Tests --

    def test_invalid_model_empty(self):
        with self.assertRaises(ValueError) as context:
            Furniture("   ", 50.0, (10, 20, 30))
        self.assertEqual(str(context.exception),
                         "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_invalid_model_too_long(self):
        long_model = "a" * 51  # 51 characters exceeds the limit.
        with self.assertRaises(ValueError) as context:
            Furniture(long_model, 50.0, (10, 20, 30))
        self.assertEqual(str(context.exception),
                         "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_set_model_valid(self):
        f = Furniture("Desk", 150.0, (80, 120, 60))
        f.model = "Office Desk"
        self.assertEqual(f.model, "Office Desk")

    def test_set_model_invalid(self):
        f = Furniture("Desk", 150.0, (80, 120, 60))
        with self.assertRaises(ValueError):
            f.model = ""

    # -- Price Property Tests --

    def test_invalid_price_negative_in_constructor(self):
        with self.assertRaises(ValueError) as context:
            Furniture("Sofa", -10.0, (100, 80, 90))
        self.assertEqual(str(context.exception), "Price must be a non-negative number.")

    def test_set_price_invalid(self):
        f = Furniture("Sofa", 100.0, (100, 80, 90))
        with self.assertRaises(ValueError):
            f.price = -5.0

    def test_set_price_valid(self):
        f = Furniture("Sofa", 100.0, (100, 80, 90))
        f.price = 120.0
        self.assertEqual(f.price, 120.0)

    # -- Dimensions Property Tests --

    def test_invalid_dimensions_length(self):
        with self.assertRaises(ValueError) as context:
            Furniture("Cabinet", 250.0, (100, 50))  # Only 2 elements.
        self.assertEqual(str(context.exception), "Dimensions tuple must contain 3 integers.")

    def test_invalid_dimensions_value_zero(self):
        with self.assertRaises(ValueError) as context:
            Furniture("Cabinet", 250.0, (100, 0, 50))
        self.assertEqual(str(context.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_invalid_dimensions_negative_value(self):
        with self.assertRaises(ValueError) as context:
            Furniture("Cabinet", 250.0, (100, -20, 50))
        self.assertEqual(str(context.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_set_dimensions_valid(self):
        f = Furniture("Cabinet", 250.0, (100, 80, 50))
        new_dims = (120, 90, 60)
        f.dimensions = new_dims
        self.assertEqual(f.dimensions, new_dims)

    def test_set_dimensions_invalid_length(self):
        f = Furniture("Cabinet", 250.0, (100, 80, 50))
        with self.assertRaises(ValueError):
            f.dimensions = (120, 90)  # Incorrect tuple length.

    def test_set_dimensions_invalid_value(self):
        f = Furniture("Cabinet", 250.0, (100, 80, 50))
        with self.assertRaises(ValueError):
            f.dimensions = (120, 0, 60)  # Contains a zero value.

    # -- Weight Property Tests --

    def test_invalid_weight_negative_in_constructor(self):
        with self.assertRaises(ValueError) as context:
            Furniture("Wardrobe", 300.0, (150, 80, 200), weight=-5.0)
        self.assertEqual(str(context.exception), "Weight must be greater than zero.")

    def test_invalid_weight_zero_in_constructor(self):
        with self.assertRaises(ValueError):
            Furniture("Wardrobe", 300.0, (150, 80, 200), weight=0)

    def test_set_weight_invalid(self):
        f = Furniture("Wardrobe", 300.0, (150, 80, 200), weight=50.0)
        with self.assertRaises(ValueError):
            f.weight = 0

    def test_set_weight_valid(self):
        f = Furniture("Wardrobe", 300.0, (150, 80, 200), weight=50.0)
        f.weight = 60.0
        self.assertEqual(f.weight, 60.0)

    def test_set_weight_to_none(self):
        f = Furniture("Wardrobe", 300.0, (150, 80, 200), weight=50.0)
        f.weight = None
        self.assertIsNone(f.weight)

    # -- get_available_status() Method Tests --

    def test_get_available_status_in_stock(self):
        f = Furniture("Lamp", 45.0, (10, 10, 30), in_stock=True)
        expected = "Model: Lamp is currently in stock."
        self.assertEqual(f.get_available_status(), expected)

    def test_get_available_status_not_in_stock(self):
        f = Furniture("Lamp", 45.0, (10, 10, 30), in_stock=False)
        expected = "Model: Lamp is currently unavailable."
        self.assertEqual(f.get_available_status(), expected)

    # -- get_specifications() Method Tests --

    def test_get_specifications_with_weight(self):
        f = Furniture("Bed", 500.0, (200, 150, 100), weight=70.0)
        expected = "Model: Bed has the following dimensions: 200mm x 150mm x 100mm and weighs: 70.0"
        self.assertEqual(f.get_specifications(), expected)

    def test_get_specifications_without_weight(self):
        f = Furniture("Bed", 500.0, (200, 150, 100), weight=None)
        expected = "Model: Bed has the following dimensions: 200mm x 150mm x 100mm and weighs: N/A"
        self.assertEqual(f.get_specifications(), expected)

if __name__ == '__main__':
    unittest.main()

