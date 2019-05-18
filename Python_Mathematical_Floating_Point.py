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
# Floating Point.
# Mitigating round-off error with increased precision.
# The use of decimal floating point eliminates decimal representation error (making it possible to represent 
# 0.1 exactly); however, some operations can still incur round-off error when non-zero digits exceed the 
# fixed precision.
# The effects of round-off error can be amplified by the addition or subtraction of nearly offsetting 
# quantities resulting in loss of significance. Knuth provides two instructive examples where rounded floating 
# point arithmetic with insufficient precision causes the breakdown of the associative and distributive
# properties of addition:
 
# Examples from Seminumerical Algorithms.

from decimal import Decimal, getcontext
    getcontext().prec = 8

    u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.51111111')
    (u + v) + w

# Displays 'Decimal('9.5111111')'

    u + (v + w)

# Displays 'Decimal('10')'

    u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
    (u*v) + (u*w)

# Displays 'Decimal('0.01')'

    u * (v+w)

# Displays 'Decimal('0.0060000')'
