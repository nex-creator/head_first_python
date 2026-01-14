import math

class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return  2*(self.width + self.height)
    
    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        line = "*" * self.width + "\n"
        return line * self.height
    def get_amount_inside(self,shape):
        times_w = self.width // shape.width
        times_h = self.height // shape.height
        return times_w * times_h

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)

    def set_height(self, height):
        self.height = height
        self.width = height

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

rectangle = Rectangle(5,10)
rectangle.set_width(20)
area = rectangle.get_area()
perimeter = rectangle.get_perimeter()
diagonal = rectangle.get_diagonal()
print(rectangle.get_picture())
print(rectangle)
print(area)
print(perimeter)
print(diagonal)
square = Square(4)
print(square)
