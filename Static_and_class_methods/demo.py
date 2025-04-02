
class Person:
    min_age = 0
    max_age = 150
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._something = "something protected"
        self.some = "not protected"

    @classmethod
    def __validate_age(cls, value):
        maxim = cls.max_age
        if value < cls.min_age:
            raise ValueError(f'{value} must be between 'f'{cls.min_age} and {maxim}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

class Employee(Person):
    min_age = 16

    # __validate_age() takes the class attribute min_age of class Employee
    def __init__(self, name, age, salary):
        super().__init__(name, age)  # when checking the age of the Employee
        self.salary = salary

    def something(self):
        return self._something

# emp = Employee("John", 65, 4645)
# person = Person("name", 56)
# print(emp.something())
# print(person._something)
# print(person.age)



