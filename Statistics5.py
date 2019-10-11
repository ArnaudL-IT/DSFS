from collections import Counter
from matplotlib import pyplot as plt
import random
from typing import List
import math
from LinearAlgebra import *

# Function definitions

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

def _median_odd(xs: List[float])->float:
    return sorted(xs)[len(xs)//2]

def _median_even(xs: List[float])->float:
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs)//2
    return (sorted_xs[hi_midpoint-1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float])->float:
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

def quantile(xs: List[float], p: float)->float:
    p_index = (int)(p*len(xs))
    return sorted(xs)[p_index]

def mode(x: List[float])->List[float]:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.item()
    if count == max_count]

def data_range(xs: List[float])->float:
    return max(xs)-min(xs)

def de_mean(xs: List[float])->float:
    """Return a list with mean == 0"""
    x_bar = mean(xs)
    return [x-x_bar for x in xs]

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def variance(xs: List[float])->float:
    assert len(xs) >= 2, 'variance requires at least two elements'
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n-1)

def standard_deviation(xs: List[float])->float:
    """The standard deviation is the squareroot of the variance"""
    return math.sqrt(variance(xs))

def interquartile_range(xs: List[float])-> float:
    """Returns the difference between the 75%-ile and the 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)

def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys)
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

def correlation(xs: List[float], ys: List[float]) -> float:
    """Measures how much xs and ys vary in tandem about their mean"""
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if(stdev_x>0 and stdev_y>0):
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0

# Main part of the program

num_friends = [random.choice(range(10)) for _ in range(100)]

friend_counts = Counter(num_friends)
xs = range(len(num_friends))
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 101])
plt.title("Histogram of Friend counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

# Some statistics

num_points = len(num_friends)
largest_value = max(num_friends)
lowest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]

print(mean(num_friends))

# Assertions are used to make sure that our function returns what we want.
# If not, an error message is shown when running the program.

assert median([1, 10, 2, 9, 5]) == 5

print(variance(num_friends))
