import unittest

from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_tuple_set_float_sum_of_ints(self):
        """
        Test that it can sum a list of integers
        """

        data = [1, 2, 3]
        result = sum(data)

        # Test a list of whole numbers
        self.assertEqual(result, 6)
        
        # Test a tuple of whole numbers
        data = (1, 2, 3)
        result = sum(data)
        self.assertEqual(result, 6)
        
        # Test a set of whole numbers
        data = {1, 2, 3}
        result = sum(data)
        self.assertEqual(result, 6)

        # Test a list of floats 
        data = (1.5, 2.5, 2)
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that is can sum a list of fractions
        """

        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 4)] 
        result = sum(data)
        self.assertEqual(result, 1)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)


# This is known as a command line entry point
if __name__ == '__main__':
    unittest.main()

# Another way to test on the commandline is to call the following command
# which runs unittest test on the test module.
# $ python -m unittest test
# $ python -m unittest -v test (verbose)   
# $ python -m unittest discover (tests any file in the folder matching test*.py)

# This allows you to test all the test files in the tests folder
# $ python -m unittest discover -s tests

# lastly if the source code you are testing is not in the root directory but is
# contained in a subdirectory for example a folder like src/ you can tell 
# unittest where to execute the test so that it can import the modules correctly
# with the -t flag
 
# $ python -m unittest discover -s tests -t src
