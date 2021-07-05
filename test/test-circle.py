import unittest
from circle import Circle

class TestCircle(unittest.TestCase):

  def test_circle_area(self):
    self.circle = Circle(2)
    area = self.circle.area()
    self.assertEqual(area, 12.56)

  def test_circle_circumference(self):
    self.circle = Circle(2)
    circumference = self.circle.circumference()
    self.assertEqual(circumference, 12.56)

if __name__=='__main__':
  unittest.main()