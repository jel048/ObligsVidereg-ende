import math
def main():
    side1 = float(input("Enter side1: "))
    side2 = float(input("Enter side2: "))
    side3 = float(input("Enter side3: "))
    
    triangle = Triangle(side1, side2, side3)
    
    color = input("Enter color: ")
    triangle.setColor(color)
    
    filled = int(input("Enter 1/0 for filled (1: true, 0: false): "))
    
    isFilled = (filled == 1)
    triangle.setFilled(isFilled)
    
    print("The area is", triangle.getArea())
    print("The perimeter is", triangle.getPerimeter())
    print("Color is", triangle.getColor())
    print("Filled is", triangle.isFilled())
class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.color = color
        self.filled = filled
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
    def isFilled(self):
        return self.filled
    def setFilled(self, filled):
        self.filled = filled
  
    def toString(self):
        return "color: " + self.color + " and filled: " + str(self.filled)
class Triangle(GeometricObject):
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise RuntimeError("Sides cannot be negative or zero.")  #OBLIG Exercise 13.11
        elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise RuntimeError("The sides cannot form a triangle.")
        else: 
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        GeometricObject.__init__(self)
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    
    def getSide3(self):
        return self.side3
    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3
    def toString(self):
        return "Triangle: side1 = " + str(self.side1) + " side2 = " + str(self.side2) + " side3 = " + str(self.side3)
main()
