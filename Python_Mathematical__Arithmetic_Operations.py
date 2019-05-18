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
# Implementing the arithmetic operations.
# We want to implement the arithmetic operations so that mixed-mode operations either call an implementation 
# whose author knew about the types of both arguments, or convert both to the nearest built in type and do 
# the operation there. 
# For subtypes of Integral, this means that __add__() and __radd__() should be defined as:
 
class MyIntegral(Integral):

    def __add__(self, other):

        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(self, other)

        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(self, other)

        else:
            return NotImplemented

    def __radd__(self, other):

        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(other, self)

        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(other, self)

        elif isinstance(other, Integral):
            return int(other) + int(self)

        elif isinstance(other, Real):
            return float(other) + float(self)

        elif isinstance(other, Complex):
            return complex(other) + complex(self)

        else:
            return NotImplemented
