from unittest import TestCase, main
from Unit_tests.mammal.project.mammal import Mammal

class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("cat1", "cat", "meow")

    def test_correct_init(self):
        self.assertEqual("cat1", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_correct_sound_is_returned_with_make_sound_method(self):
        result = self.mammal.make_sound()
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", result)

    def test_get_kingdom_method(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info_method_returns_correct_string(self):
        result = self.mammal.info()
        self.assertEqual("cat1 is of type cat", result)


if __name__=="__main__":
    main()