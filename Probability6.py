import matplotlib.pyplot as plt
import math
from collections import Counter
import random

def uniform_pdf(x: float)->float:
    if 0<x<1: return 1
    else: return 0

def uniform_cdf(x: float)->float:
    """Returns the probability that a uniform random variable is <=x"""
    if x<0:
        return 0
    elif x<1:
        return x
    else:
        return 1

SQRT_TWO_PI = math.sqrt(2.0 * math.pi)

def normal_pdf(x: float, mu: float = 0, sigma: float = 1)->float:
    return (math.exp(-(x-mu)**2 / (2.0 * sigma**2)) / (sigma * SQRT_TWO_PI))

def normal_cdf(x: float, mu: float = 0, sigma: float = 1)->float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001)->float:
    """Find approximate inverse using binary search"""
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance = tolerance)

    low_z = -10.0
    hi_z = 10.0
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        else:
            hi_z = mid_z

    return mid_z

def bernouilli_trial(p: float)->int:
    """Returns 1 with probablility p and 0 with probability (1-p)"""
    return 1 if random.random()<p else 0

def binomial(n: int, p: float)->int:
    """Returns the sum of n Bernouilli(p) trials"""
    return sum(bernouilli_trial(p) for _ in range(n))

def binomial_histogram(p: float, n: int, num_points: int)->None:
    """Picks points from a Binomial(n, p) and plots their histogram"""
    data = [binomial(n, p) for _ in range(num_points)]

    #use a bar chart to show the binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()], [v/num_points for v in histogram.values()], 0.8, color = '0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1-p))

    #use a line chart to show the normal approximation
    xs = range(min(data), max(data)+1)
    ys = [normal_cdf(i+0.5, mu, sigma) - normal_cdf(i-0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial distribution vs. Normal approximation")
    plt.show()

####################

xs = [ x / 10.0 for x in range(-50,50)]
plt.plot(xs, [normal_pdf(x, sigma = 1) for x in xs], '-', label = 'mu=0, sigma=1')
plt.plot(xs, [normal_pdf(x, sigma = 0.5) for x in xs], '--', label = 'mu=0, sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma = 2) for x in xs], ':', label = 'mu=0, sigma=2')
plt.plot(xs, [normal_pdf(x, mu = -1) for x in xs], '-.', label = 'mu=-1, sigma=1')
plt.legend()
plt.title('Various Normal PDFs')
plt.show()

plt.plot(xs, [normal_cdf(x, sigma = 1) for x in xs], '-', label = 'mu=0, sigma=1')
plt.plot(xs, [normal_cdf(x, sigma = 0.5) for x in xs], '--', label = 'mu=0, sigma=0.5')
plt.plot(xs, [normal_cdf(x, sigma = 2) for x in xs], ':', label = 'mu=0, sigma=2')
plt.plot(xs, [normal_cdf(x, mu = -1) for x in xs], '-.', label = 'mu=-1, sigma=1')
plt.legend(loc=4)
plt.title('Various Normal CDFs')
plt.show()

binomial_histogram(0.75, 100, 10000)
