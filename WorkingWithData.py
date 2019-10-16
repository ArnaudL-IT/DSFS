from typing import List, Dict
from collections import Counter
import math

import matplotlib.pyplot as plt

def bucketize(point: float, bucket_size: float)->float:
    """Floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points: List[float], bucket_size: float)->Dict[float, int]:
    """Bucket the points and count how many of them in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points: List[float], bucket_size: float, title: str = ""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width = bucket_size)
    plt.title(title)
    plt.show()

import random
from Probability import inverse_normal_cdf

random.seed(0)

uniform = [200 * random.random() - 100 for _ in range(10000)]
normal = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]

plot_histogram(uniform, 10, "Uniform histogram")
plot_histogram(normal, 10, "Normal histogram")

#########################################################################

def random_normal()->float:
    """Returns a random draw from a standard normal distribution"""
    return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]

plt.scatter(xs, ys1, marker = '.', color="black", label="ys1")
plt.scatter(xs, ys2, marker = '.', color="red", label="ys2")
plt.xlabel("xs")
plt.ylabel("ys")
plt.legend(loc=9)
plt.title("Very different joint distributions")
plt.show()

#########################################################################

from Statistics import correlation

print(correlation(xs, ys1))
print(correlation(xs, ys2))

#########################################################################

from LinearAlgebra import Matrix, Vector, make_matrix

def correlation_matrix(data : List[Vector])->Matrix:
    """Returns the len(data)*len(data) matrix whose (i, j)-th entry is the correlation between data[i] and data[j]"""
    def correlation_ij(i: int, j: int)->float:
        return correlation(data[i], data[j])

    return make_matrix(len(data), len(data), correlation_ij)

corr_data = [[random.random() for _ in range(100)], [math.floor(random.random()) + 1 for _ in range(100)], [4 for _ in range(100)], [random_normal()  for _ in range(100)]]

num_vectors = len(corr_data)
fig, ax = plt.subplots(num_vectors, num_vectors)

for i in range(num_vectors):
    for j in range(num_vectors):
        if i != j: ax[i][j].scatter(corr_data[j], corr_data[i])
        else: ax[i][j].annotate("series " + str(i), (0.5, 0.5), ha="center", va="center")

        if i < num_vectors - 1: ax[i][j].xaxis.set_visible(False)
        if j >> 0: ax[i][j].yaxis.set_visible(False)

ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
ax[0][0].set_ylim(ax[0][1].get_ylim())

plt.show()
