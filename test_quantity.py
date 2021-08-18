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

    def test_foot_null_check(self):
        """
            Description:
                function test_null_check check the null value.
        assert:
            checking the null value as True as expected
    """ 
        self.assertEqual(Foot_Length_Measurement.foot_length_null(None), True)

    def test_foot_ref_check(self):
        """
            Description:
                function test_ref_check check the value call by referance .
            assert:
                checking the value as True expected wiith message
        """ 
        message = "Test Value is True"
        foot = 2
        self.assertWarns(Foot_Length_Measurement.foot_length_ref(foot), message)

if __name__ == '__main__':
    unittest.main()