from project.volcano import Volcano

from unittest import TestCase, main

class TestVolcano(TestCase):

    def setUp(self):
        Volcano._unique_names = set()

    def test_valid_init(self):
        vol = Volcano("VOLCANO1", 3329, 2020)
        self.assertEqual(vol.name, "VOLCANO1")
        self.assertEqual(vol.height_m, 3329)
        self.assertEqual(vol.last_eruption, 2020)

    def test_name_stripping_and_uppercasing(self):
        vol = Volcano("  volcano1 ", 1247)
        self.assertEqual(vol.name, "VOLCANO1")

    def test_invalid_name_too_short(self):
        with self.assertRaises(ValueError) as ex:
            Volcano(" a ", 1000)
        self.assertEqual(str(ex.exception), "Volcano name must be at least two characters long!")

    def test_invalid_name_only_whitespace(self):
        with self.assertRaises(ValueError) as cm:
            Volcano("   ", 1500)
        self.assertEqual(str(cm.exception), "Volcano name must be at least two characters long!")

    def test_name_uniqueness(self):
        vol1 = Volcano("volcano", 1245)
        with self.assertRaises(ValueError) as ex:
            Volcano("  volcano", 1234)
        self.assertEqual(str(ex.exception), "Volcano name must be unique!")

    def test_invalid_height_zero(self):
        with self.assertRaises(ValueError) as cm:
            Volcano("Mauna Loa", 0)
        self.assertEqual(str(cm.exception), "Height must be a positive integer!")

    def test_invalid_height_negative(self):
        with self.assertRaises(ValueError) as ex:
            Volcano("volcano123", -1)
        self.assertEqual(str(ex.exception), "Height must be a positive integer!")

    def test_invalid_height_zero_value(self):
        with self.assertRaises(ValueError) as ex:
            Volcano("volcano123", 0)
        self.assertEqual(str(ex.exception), "Height must be a positive integer!")

    def test_is_active_when_recent_eruption(self):
        vol = Volcano("volcanoactive", 1234, 2001)
        self.assertTrue(vol.is_active)

    def test_is_not_active_due_to_old_eruption(self):
        vol = Volcano("volcanoinactive", 1234, 1980)
        self.assertFalse(vol.is_active)

    def test_is_not_active_when_no_eruption(self):
        vol = Volcano("volcanoinactive", 1234)
        self.assertFalse(vol.is_active)

    def test_unique_volcano_count(self):
        self.assertEqual(Volcano.unique_volcano_count(), 0)
        v1 = Volcano("volcano", 1234)
        self.assertEqual(Volcano.unique_volcano_count(), 1)
        v2 = Volcano("VOLCANO1", 1234)
        self.assertEqual(Volcano.unique_volcano_count(), 2)


if __name__=="__main__":
    main()
