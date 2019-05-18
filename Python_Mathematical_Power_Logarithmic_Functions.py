# Python Numeric and Mathematical Modules.
# numbers — Numeric abstract base classes.
# The numbers module (PEP 3141) defines a hierarchy of numeric abstract base classes which 
# progressively define more operations. None of the types defined in this module can be 
# instantiated.
# math — Mathematical functions.
# This module is always available. It provides access to the mathematical functions defined 
# by the C standard.
# cmath — Mathematical functions for complex numbers.
# This module is always available. It provides access to mathematical functions for complex numbers. 
# The functions in this module accept integers, floating-point numbers or complex numbers as arguments.
# decimal — Decimal fixed point and floating point arithmetic.
# The decimal module provides support for fast correctly-rounded decimal floating point arithmetic. 
# It offers several advantages over the float datatype:
# random — Generate pseudo-random numbers
# This module implements pseudo-random number generators for various distributions.
# statistics — Mathematical statistics functions.
# This module provides functions for calculating mathematical statistics of numeric (Real-valued) data.
# Power and logarithmic functions.
# math.exp(x). 
# Return e raised to the power x, where e = 2.718281… is the base of natural logarithms. 
# This is usually more accurate than math.e ** x or pow(math.e, x).
# math.expm1(x) 
# Return e raised to the power x, minus 1. Here e is the base of natural logarithms. 
# For small floats x, the subtraction in exp(x) - 1 can result in a significant loss of precision; the expm1() 
# function provides a way to compute this quantity to full precision:
 
from math import exp, expm1

    exp(1e-5) - 1  # Gives result accurate to 11 places
                   # Displays '1.0000050000069649e-05'

    expm1(1e-5)    # result accurate to full precision
                   # Displays '1.0000050000166668e-05'
