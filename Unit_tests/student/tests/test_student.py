from unittest import TestCase, main

from Unit_tests.student.project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Student1", {"OOP": ["Inheritance, Encapsulation"]})
        self.student1 = Student("Student1")

    def test_correct_init(self):
        self.assertEqual("Student1", self.student.name)
        self.assertEqual({"OOP": ["Inheritance, Encapsulation"]}, self.student.courses)
        self.assertEqual({}, self.student1.courses)

    def test_enrolling_in_a_course_student_is_already_in_should_update_notes_and_return_string(self):
        result = self.student.enroll("OOP", ["Polymorphism", "Abstraction"])

        self.assertEqual(["Inheritance, Encapsulation", "Polymorphism", "Abstraction"], self.student.courses["OOP"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_in_a_new_class_and_add_notes_to_it_return_string_and_validate_added_notes_and_course(self):
        result = self.student1.enroll("OOP", ["Polymorphism", "Abstraction"], "Y")
        result1 = self.student.enroll("Math", ["Algebra"], "")

        self.assertEqual({"OOP":["Polymorphism", "Abstraction"]}, self.student1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["Algebra"], self.student.courses["Math"])
        self.assertEqual("Course and course notes have been added.", result1)

    def test_enroll_in_class_but_dont_add_notes_returns_string_and_adds_empty_notes_list_to_class(self):
        result = self.student1.enroll("OOP", ["Polymorphism", "Abstraction"], "N")
        self.assertEqual({"OOP": []}, self.student1.courses)
        self.assertEqual("Course has been added.", result)

    def test_adding_notes_on_existing_class_checks_notes_and_if_correct_str_is_returned(self):
        result = self.student.add_notes("OOP", "Polymorphism")
        self.assertEqual({"OOP": ["Inheritance, Encapsulation", "Polymorphism"]}, self.student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_not_existing_class_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student1.add_notes("OOP", "Polymorphism")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_student_was_enrolled_in_removes_the_course_and_returns_string(self):
        result = self.student.leave_course("OOP")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leave_course_student_was_enrolled_in_removes_the_course_and_returns_string(self):
        with self.assertRaises(Exception) as ex:
            self.student1.leave_course("OOP")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__=="__main__":
    main()