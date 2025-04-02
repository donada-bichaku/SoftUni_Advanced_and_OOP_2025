class Shape:

    def area_x(self):
        pass

class Circle:

    def area(self):
        return "circle area"


class Square:

    def area(self):
        return "square area"

    def area(self, num):
        return "square area"

a= Square()
a.area()
a.area(3)

shapes = [Circle(), Square(), Square()]
for s in shapes:
    print(s.area())