import unittest
import calc

class TestEmployee(unittest.TestCase):

    Employee emp1 = Employee("Sam", "Palmer")
    Employee emp2 = Employee()
    emp2.first = "Sam"
    emp2.last = "Palmer" 
    
    # Puzzle: Work out a test for the backward compatibility of the 
    # @propertys in the Employee class
    
   # def test_add(self):
   #     self.assertEqual(calc.add(10, 5), 15)
   #     self.assertEqual(calc.add(-1, 1), 0)
   #     self.assertEqual(calc.add(-1, -1), -2)

   #         calc.divide(10,0):


if __name__ == '__main__':
    unittest.main()
