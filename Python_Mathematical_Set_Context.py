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
# Working with threads.
# The getcontext() function accesses a different Context object for each thread. Having separate thread 
# contexts means that threads may make changes (such as getcontext().prec=10) without interfering with 
# other threads.
# Likewise, the setcontext() function automatically assigns its target to the current thread.
# If setcontext() has not been called before getcontext(), then getcontext() will automatically create a
# new context for use in the current thread.
# The new context is copied from a prototype context called DefaultContext. To control the defaults so 
# that each thread will use the same values throughout the application, directly modify the DefaultContext 
# object. This should be done before any threads are started so that there won’t be a race condition 
# between threads calling getcontext().
 
# Set applicationwide defaults for all threads about to be launched

DefaultContext.prec = 12
DefaultContext.rounding = ROUND_DOWN
DefaultContext.traps = ExtendedContext.traps.copy()
DefaultContext.traps[InvalidOperation] = 1

setcontext(DefaultContext)

# Afterwards, the threads can be started

t1.start()
t2.start()
t3.start()
