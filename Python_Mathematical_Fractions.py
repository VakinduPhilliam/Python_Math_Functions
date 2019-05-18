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

from fractions import Fraction
Fraction(16, -10)

Fraction(123)

Fraction()

Fraction('3/7')

Fraction(' -3/7 ')

Fraction('1.414213 \t\n')

Fraction('-.125')

Fraction('7e-6')

Fraction(2.25)

Fraction(1.1)

from decimal import Decimal
Fraction(Decimal('1.1'))

