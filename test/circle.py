class Shapes():
  pi = 3.14

  def __init__(self):
    pass

  def circumference(self):
    print("I dont know my circumference")
  
  def area(self):
    print("I dont know my area")

  def printShape(self, shape):
    print(f"{shape} is my shape")

  def whoami(self):
    print(f"I dontknow is my shape")

class Circle(Shapes):

  def __init__(self, radius=1):
    Shapes.__init__(self)
    self.radius = radius

  def __str__(self):
    return "Im a circle of radius {}".format(self.radius)

  def __len__(self):
    return self.radius

  def circumference(self):
    self.printShape("circle")
    return self.radius * 2 * Shapes.pi
  
  def area(self):
    self.printShape("circle")
    return Shapes.pi * (self.radius ** 2)

  def whoami(self, param):
    print("circle is my shape", param)



if __name__=='__main__':
  circle1 = Circle(30)
  print(circle1.area())
  print(circle1.circumference())
  circle1.printShape("saru")
  circle1.whoami("la")
  print(str(circle1))
  print(len(circle1))
  print(circle1)


