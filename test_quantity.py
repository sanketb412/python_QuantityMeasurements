# ''""
# @Author: Sanket Bagde
# @Date: 2021-16-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python TEST CASE to check length measrements.
# '''

import unittest
from quantity_measure import Foot_Length_Measurement

class MyTestCases(unittest.TestCase):        
    def test_foot_lenght_equality(self):
        """
            Description:
                function test_length_equality check the equality of the inputs thats return the boolean value.
            assert:
                comparing the inputs to be equal and returning True as expected
        """ 
        self.assertEqual(Foot_Length_Measurement.foot_length_equality(1,1), True)


if __name__ == '__main__':
    unittest.main()