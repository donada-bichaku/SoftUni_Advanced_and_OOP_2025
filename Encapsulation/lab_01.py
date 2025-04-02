# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self. __age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


person = Person("George", 23)
print(person.age)
print(person.name)