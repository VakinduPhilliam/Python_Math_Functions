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
# Notes for type implementors 
# Implementors should be careful to make equal numbers equal and hash them to the same values. 
# This may be subtle if there are two different extensions of the real numbers. 
# For example, fractions.Fraction implements hash() as follows:
 
def __hash__(self):

    if self.denominator == 1:

        # Get integers right.

        return hash(self.numerator)

    # Expensive check, but definitely correct.

    if self == float(self):
        return hash(float(self))

    else:

        # Use tuple's hash to avoid a high collision rate on
        # simple fractions.

        return hash((self.numerator, self.denominator))
