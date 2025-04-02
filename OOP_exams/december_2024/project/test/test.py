from project.gallery import Gallery
import unittest


class TestGallery(unittest.TestCase):
    def setUp(self):
        # Create a valid Gallery instance for most tests.
        self.gallery = Gallery("Gallery123", "NewYork", 100.0)

    def test_valid_construction(self):
        # Check that all properties are set correctly.
        self.assertEqual(self.gallery.gallery_name, "Gallery123")
        self.assertEqual(self.gallery.city, "NewYork")
        self.assertEqual(self.gallery.area_sq_m, 100.0)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual(self.gallery.exhibitions, {})

    def test_invalid_gallery_name(self):
        # Gallery name must be alphanumeric after stripping.
        with self.assertRaises(ValueError) as cm:
            Gallery("Invalid Name!", "City", 50.0)
        self.assertEqual(str(cm.exception), "Gallery name can contain letters and digits only!")

    def test_invalid_city(self):
        # City must start with a letter and cannot be empty.
        with self.assertRaises(ValueError) as cm:
            Gallery("Gallery123", "1City", 50.0)
        self.assertEqual(str(cm.exception), "City name must start with a letter!")

        with self.assertRaises(ValueError) as cm:
            Gallery("Gallery123", "", 50.0)
        self.assertEqual(str(cm.exception), "City name must start with a letter!")

    def test_invalid_area(self):
        # Area must be a positive number.
        with self.assertRaises(ValueError) as cm:
            Gallery("Gallery123", "City", 0.0)
        self.assertEqual(str(cm.exception), "Gallery area must be a positive number!")

        with self.assertRaises(ValueError) as cm:
            Gallery("Gallery123", "City", -10.0)
        self.assertEqual(str(cm.exception), "Gallery area must be a positive number!")

    def test_gallery_name_setter_trimming(self):
        # Test that gallery_name setter trims the value.
        g = Gallery("Gallery123", "City", 50.0)
        g.gallery_name = "   NewName456  "
        self.assertEqual(g.gallery_name, "NewName456")

    def test_add_exhibition(self):
        # Test adding a new exhibition.
        result = self.gallery.add_exhibition("ExhibitA", 2020)
        self.assertEqual(result, 'Exhibition "ExhibitA" added for the year 2020.')
        # Test adding the same exhibition again.
        duplicate_result = self.gallery.add_exhibition("ExhibitA", 2021)
        self.assertEqual(duplicate_result, 'Exhibition "ExhibitA" already exists.')
        # Check that the original year remains unchanged.
        self.assertEqual(self.gallery.exhibitions["ExhibitA"], 2020)

    def test_remove_exhibition(self):
        # Test removing an exhibition that doesn't exist.
        result = self.gallery.remove_exhibition("ExhibitB")
        self.assertEqual(result, 'Exhibition "ExhibitB" not found.')
        # Add an exhibition and then remove it.
        self.gallery.add_exhibition("ExhibitA", 2020)
        result_remove = self.gallery.remove_exhibition("ExhibitA")
        self.assertEqual(result_remove, 'Exhibition "ExhibitA" removed.')
        self.assertNotIn("ExhibitA", self.gallery.exhibitions)

    def test_list_exhibitions_open(self):
        # When open, list_exhibitions should return a list of exhibitions.
        # If no exhibitions, expect an empty string.
        self.assertEqual(self.gallery.list_exhibitions(), "")
        # Add some exhibitions.
        self.gallery.add_exhibition("ExhibitA", 2020)
        self.gallery.add_exhibition("ExhibitB", 2021)
        listing = self.gallery.list_exhibitions()
        # Check that both exhibitions appear in the result.
        self.assertIn("ExhibitA: 2020", listing)
        self.assertIn("ExhibitB: 2021", listing)

    def test_list_exhibitions_closed(self):
        # When gallery is closed to the public.
        g = Gallery("Gallery123", "City", 50.0, open_to_public=False)
        self.assertEqual(
            g.list_exhibitions(),
            'Gallery Gallery123 is currently closed for public! Check for updates later on.'
        )


if __name__ == '__main__':
    unittest.main()
