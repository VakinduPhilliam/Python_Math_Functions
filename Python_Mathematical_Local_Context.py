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
# decimal.localcontext(ctx=None). 
# Return a context manager that will set the current context for the active thread to a copy of ctx on 
# entry to the with-statement and restore the previous context when exiting the with-statement. 
# If no context is specified, a copy of the current context is used.
# For example, the following code sets the current decimal precision to 42 places, performs a calculation,
# and then automatically restores the previous context:
 
from decimal import localcontext

with localcontext() as ctx:

    ctx.prec = 42   # Perform a high precision calculation

    s = calculate_something()

s = +s  # Round the final result back to the default precision
