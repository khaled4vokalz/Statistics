from helper import num_friends, sum_of_squares
ct = __import__('01_central_tendencies')

import math

# Dispersion refers to measures of how spread out our data is. 
# Typically they're statistics for which values near zero signify not spread out at all 
# and for which large values (whatever that means) signify very spread out
def data_range(x):
    return max(x) - min(x)

print(data_range(num_friends))

print("Mean:",ct.mean(num_friends))

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = ct.mean(x)
    de_meaned_list = [x_i - x_bar for x_i in x]
    print(ct.mean(de_meaned_list))                          # now mean(x) should be 0
    return de_meaned_list

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):    
    return math.sqrt(variance(x))                           # as the variance holds the squared values 
                                                            # we sqrt it to make sense of the unit with others (mean, median etc.)

def interquartile_range(x):    
    return ct.quantile(x, 0.75) - ct.quantile(x, 0.25)      # as quantile is sorted, so the outliers won't affect this range so much

print(num_friends)
print(de_mean(num_friends))
print(variance(num_friends))
print(standard_deviation(num_friends))