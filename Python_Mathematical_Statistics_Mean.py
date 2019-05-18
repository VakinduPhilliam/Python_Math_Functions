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
# statistics.mean(data).
# Return the sample arithmetic mean of data which can be a sequence or iterator.
# The arithmetic mean is the sum of the data divided by the number of data points. 
# It is commonly called “the average”, although it is only one of many different mathematical averages. 
# It is a measure of the central location of the data.
# If data is empty, StatisticsError will be raised.
 
mean([1, 2, 3, 4, 4])

# Displays '2.8'

mean([-1.0, 2.5, 3.25, 5.75])

# Displays '2.625'

from fractions import Fraction as F
mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])

# Displays 'Fraction(13, 21)'

from decimal import Decimal as D
mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])

# Displays 'Decimal('0.5625')'
