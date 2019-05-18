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

# statistics.harmonic_mean(data) 
# Return the harmonic mean of data, a sequence or iterator of real-valued numbers.
# The harmonic mean, sometimes called the subcontrary mean, is the reciprocal of the arithmetic mean() of 
# the reciprocals of the data. For example, the harmonic mean of three values a, b and c will be equivalent 
# to 3/(1/a + 1/b + 1/c).
# The harmonic mean is a type of average, a measure of the central location of the data. It is often appropriate 
# when averaging quantities which are rates or ratios, for example speeds. For example:
# Suppose an investor purchases an equal value of shares in each of three companies, with P/E (price/earning)
# ratios of 2.5, 3 and 10. What is the average P/E ratio for the investor’s portfolio?
 
harmonic_mean([2.5, 3, 10])  # For an equal investment portfolio.
                             # Displays '3.6'

# statistics.median(data) 
# Return the median (middle value) of numeric data, using the common “mean of middle two” method. If data is empty, 
# StatisticsError is raised. data can be a sequence or iterator.
# The median is a robust measure of central location, and is less affected by the presence of outliers in your data. 
# When the number of data points is odd, the middle data point is returned:
 
median([1, 3, 5])
                 
# Displays '3'

# statistics.median_low(data) 
# Return the low median of numeric data. If data is empty, StatisticsError is raised. data can be a sequence or iterator.
# The low median is always a member of the data set. When the number of data points is odd, the middle value is returned. 
# When it is even, the smaller of the two middle values is returned.
 
median_low([1, 3, 5])

# Displays '3'

median_low([1, 3, 5, 7])

# Displays '3'

# statistics.median_high(data) 
# Return the high median of data. If data is empty, StatisticsError is raised. data can be a sequence or iterator.
# The high median is always a member of the data set. When the number of data points is odd, the middle value is returned. 
# When it is even, the larger of the two middle values is returned.
# Use the high median when your data are discrete and you prefer the median to be an actual data point rather than 
# interpolated.
 
median_high([1, 3, 5])

# Displays '3'

median_high([1, 3, 5, 7])

# Displays '5'
 
# statistics.median_grouped(data, interval=1) 
# Return the median of grouped continuous data, calculated as the 50th percentile, using interpolation. If data is empty, 
# StatisticsError is raised. data can be a sequence or iterator.

median_grouped([52, 52, 53, 54])

# Displays '52.5'

# statistics.mode(data). 
# Return the most common data point from discrete or nominal data. The mode (when it exists) is the most typical value, and 
# is a robust measure of central location.
# If data is empty, or if there is not exactly one most common value, StatisticsError is raised.
# 'mode' assumes discrete data, and returns a single value. This is the standard treatment of the mode as commonly taught 
# in schools:
 
mode([1, 1, 2, 3, 3, 3, 3, 4])

# Displays '3'
 
# The mode is unique in that it is the only statistic which also applies to nominal (non-numeric) data:
 
mode(["red", "blue", "blue", "red", "green", "red", "red"])

# Displays'red'

# statistics.pstdev(data, mu=None). 
# Return the population standard deviation (the square root of the population variance). See pvariance() for arguments and other 
# details.
 
pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])

# Displays '0.986893273527251'

# statistics.pvariance(data, mu=None). 
# Return the population variance of data, a non-empty iterable of real-valued numbers. Variance, or second moment about the mean,
# is a measure of the variability (spread or dispersion) of data. A large variance indicates that the data is spread out; a small 
# variance indicates it is clustered closely around the mean.
# If the optional second argument mu is given, it should be the mean of data. If it is missing or None (the default), the mean is 
# automatically calculated.
# Use this function to calculate the variance from the entire population. To estimate the variance from a sample, the variance() 
# function is usually a better choice.
# Raises StatisticsError if data is empty.
 

data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
pvariance(data)

# Displays '1.25'

# Statistics.pvariance also supports decimals and fractions.
 
from decimal import Decimal as D
pvariance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])

# Displays 'Decimal('24.815')'

from fractions import Fraction as F
pvariance([F(1, 4), F(5, 4), F(1, 2)])

# Displays 'Fraction(13, 72)'

# statistics.stdev(data, xbar=None) 
# Return the sample standard deviation (the square root of the sample variance). See variance() for arguments and other details.
 
stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])

# Displays '1.0810874155219827'

# statistics.variance(data, xbar=None) 
# Return the sample variance of data, an iterable of at least two real-valued numbers. Variance, or second moment about the mean,
# is a measure of the variability (spread or dispersion) of data. A large variance indicates that the data is spread out; a small 
# variance indicates it is clustered closely around the mean.
# If the optional second argument xbar is given, it should be the mean of data. If it is missing or None (the default), the mean is 
# automatically calculated.
# Use this function when your data is a sample from a population. To calculate the variance from the entire population, see pvariance().
# Raises StatisticsError if data has fewer than two values.
 
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
variance(data)

# Displays '1.3720238095238095'
 
# If you have already calculated the mean of your data, you can pass it as the optional second argument xbar to avoid recalculation:
 

m = mean(data)
variance(data, m)

# Displays '1.3720238095238095'
 
# This function does not attempt to verify that you have passed the actual mean as xbar. 
# Using arbitrary values for xbar can lead to invalid or impossible results.
# Decimal and Fraction values are supported:
 
from decimal import Decimal as D
variance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])

# Displays 'Decimal('31.01875')'

from fractions import Fraction as F
variance([F(1, 6), F(1, 2), F(5, 3)])

# Displays 'Fraction(67, 108)'
