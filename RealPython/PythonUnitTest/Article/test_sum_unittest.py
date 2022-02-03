# https://realpython.com/python-testing/

# 1. Import unittest from the standard library
import unittest

# Create a class called Test_Sum that inherits from TestCase class
class Test_Sum(unittest.TestCase):

    # Convert the functions into methods by adding self as an argument
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    def test_sum_tuple(self):

        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

# So if we think about the heirachy a little bit here: 
# unittest -> TestCase -> Test_Sum
# and from our understanding of inheritance with the whole point being 
# that we don't repeat code we can say Test_Sum 'is' a unittest. This sounds
# very pythonic :) 
# Presumably when unittest call the main() method it then calls all the methods
# in itself that start with test. Something like that.

# I've also installed nose2 so from the command line you can also call the test
# Command: python -m nose2
