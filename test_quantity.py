# ''""
# @Author: Sanket Bagde
# @Date: 2021-16-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python TEST CASE to check length measrements.
# '''

import unittest
from quantity_measure import Foot_Length_Measurement,Inch_Length_Measurement,Foot_Inch_Measurement,Foot_Yard_Measurement

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

    # def test_foot_ref_check(self):
    #     """
    #         Description:
    #             function test_ref_check check the value call by referance .
    #         assert:
    #             checking the value as True expected wiith message
    #     """ 
    #     message = "Test Value is True"
    #     foot = 2
    #     self.assertWarns(Foot_Length_Measurement.foot_length_ref(foot), message)

    def test_foot_type_check(self):
        """
            Description:
                function test_type_check check the type of the input.
            assert:
                matching the type of the input value and return value
        """ 
        self.assertEqual(Foot_Length_Measurement.foot_length_type(2), int)

    def test_foot_value_check(self):
        """
            Description:
                function test_value_check check the value of the conversion.
            assert:
                checking the value as expected for inch
        """ 
        self.assertEqual(Foot_Length_Measurement.foot_length_value(3), 36)


# checking for Inch to Foot

    def test_inch_length_measure(self):
        """
            Description:
                function test_length_measure compare the length which gets returns and the actuall value 24.
            assert:
                returning the convertable value from foot to inch
        """ 
        self.assertEqual(Inch_Length_Measurement.inch_length_comparision(24), 2)
        
    def test_inch_ref_check(self):
        """
            Description:
                function test_ref_check check the value call by referance .
            assert:
                checking the value as True expected wiith message
        """ 
        message = "Test Value is True"
        foot = 2
        self.assertWarns(Inch_Length_Measurement.inch_length_ref(foot), message)

    def test_inch_type_check(self):
        """
            Description:
                function test_type_check check the type of the input.
            assert:
                matching the type of the input value and return value
        """ 
        self.assertEqual(Inch_Length_Measurement.inch_length_type(60), int)

    def test_inch_value_check(self):
        """
            Description:
                function test_value_check check the value of the conversion.
            assert:
                checking the value as expected for inch
        """ 
        self.assertEqual(Inch_Length_Measurement.inch_length_value(36), 3)

# checking foot and inch equal values

    def test_foot_inch_check(self):
        """
            Description:
                function test_foot_inch_check check the value of foot and inch to return equal value.
            assert:
                checking the value as expected True
        """ 
        self.assertEqual(Foot_Inch_Measurement.foot_inch_value(0, 0), True)

# comparing length like happy and sad cases

    def test_ft_in_comapring_length(self):
        self.assertNotEqual(Foot_Inch_Measurement.happy_sad_foot_case(1), 1)
        self.assertEqual(Foot_Inch_Measurement.happy_sad_foot_case(1), 12)
    
    def test_in_ft_comapring_length(self):
        self.assertNotEqual(Foot_Inch_Measurement.happy_sad_inch_case(1), 1)
        self.assertEqual(Foot_Inch_Measurement.happy_sad_inch_case(12), 1)

# comapring foot inch yard like happy sad test

    def test_ft_yd_comparing_length(self):
        self.assertEqual(Foot_Yard_Measurement.happy_sad_foot_yard_case(3), 1)
        self.assertNotEqual(Foot_Yard_Measurement.happy_sad_foot_yard_case(1), 1)

if __name__ == '__main__':
    unittest.main()