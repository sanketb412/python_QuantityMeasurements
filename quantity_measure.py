# ''""
# @Author: Sanket Bagde
# @Date: 2021-16-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python to check length measrements.
# '''

print("Welcome to Quantity Measure Program.")
class Foot_Length_Measurement():
    """
        A class to represent a Length Measurements.
        ...
        Attributes
        ----------
        its not taking any attributes
        ...
        Methods
        -------
        # foot_length_comparision(foot):
        # foot_length_equality(foot, inch)
        # foot_length_null(foot)
        # foot_length_type(foot)
        # foot_length_value(foot)
    """ 
    def foot_length_comparision(foot):
        """
            Description:
                function length_comparision compare the length between foot to inch. with taking one input as an argument
            Parameter:
                foot as an input
            Return:
                printing the convertable value from foot to inch
        """ 
        try:
            foot = 1
            inch = 12*foot
            print("1 foot = ", inch, "inch")
        except Exception:
            print(Exception)

if __name__=='__main__':
    foot_obj = Foot_Length_Measurement()
    foot_obj.foot_length_comparision()
