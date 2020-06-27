import unittest
import activities 
from activities import add

class Testcalc(unittest.TestCase):
     
     def test_Add(self):
         self.assertEqual(
              activities.add(10, 5), 15,
                          msg="asserted func run test"
                          )
         self.assertEqual(
             activities.add(-1, -1), -2,
             msg="asserted func run test"
         )
         self.assertEqual(
             activities.add(-1, 1), 0,
             msg="asserted func run test"
         )
     def test_subtarct(self):
          self.assertEqual(activities.subtract(1,1),0)

     def test_sub(self):
         self.assertEqual(activities.subtract(-1, 1), -2)
if __name__ == '__main__':
     unittest.main()
