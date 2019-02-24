from helper import num_friends
from collections import Counter

def mean(x):                                # mean is just the average of the list contents
    return sum(x)/len(x)

print("Mean:",mean(num_friends))            # this will be different everytime we run the file as 
                                            # we are generating random integer numbers for 'num_friends'
                                            # list everytime. However the value of this totally depends
                                            # on each of the data point i.e. list value

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)                    # this is one way of finding the median by sorting the list
                                            # there can be other ways but that's not important for our
                                            # cause
    midpoint = n // 2

    if(n % 2) == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

print("Median:", median(num_friends))      # median depends on the middle most / middle two values
                                           # values of the list, if those doesn't change then the
                                           # median will be same even if other data points are changed


# Percentile: the value below which a percentage of data falls
# e.g.: You are the fourth tallest person in a group of 20
# 80% of people are shorter than you
# That means you are at the 80th percentile.
# If your height is 1.85m then "1.85m" is the 80th percentile height in that group
def quantile(x, p):
    """returns the p-th percentile value in x where x is the vector"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

print("10-th quantile:", quantile(num_friends, 0.10))
print("25-th quantile:", quantile(num_friends, 0.25))
print("75-th quantile:", quantile(num_friends, 0.75))
print("90-th quantile:", quantile(num_friends, 0.90))

def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]

print("Mode:", mode(num_friends))