class Shape:
    def init(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def perimeter(self):
        return 2 * (self._length + self._width)
    def display_shape_type(self):
        print(f"This is a shape of type: {self._name}")
    def display_shape_type(self):
        self.__display_shape_type()

class Rectangle(Shape):
    def __init(self, length, width):
        super().init("Rectangle")
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return 2 * (self.__length + self.__width)
    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width


Rec1 = Rectangle(20.34, 10.20)

print(Rec1.area())
print(Rec1.perimeter())
print(Rec1.get_name())
Rec1.display_shape_type()
Rec1.__display_shape_type()

print("Length:", Rec1.get_length())
print("Width:", Rec1.get_width())