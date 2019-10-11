from LinearAlgebra import Vector, dot, distance, add, scalar_multiply
from typing import Callable
import random

def difference_quotient(f: Callable[[float], float], x: float, h: float)->float:
    return (f(x+h) - f(x)) / h

def partial_difference_quotient(f: Callable[[Vector], float], v: Vector, i: int, h: float)->float:
    """Returns the ith partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0)
    for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h

def estimate_gradient(f: Callable[[Vector], float], v: Vector, h: float = 0.0001):
    return [partial_difference_quotient(f, v, i, h) for i in range(len(v))]

def square(x: float)->float:
    return x**2

def derivative(x: float)->float:
    return 2*x

xs = range(-10, 11)
actuals = [derivative(x) for x in xs]
estimates = [difference_quotient(square, x, h=0.001) for x in xs]

#plot to show that tey are basically the same
import matplotlib.pyplot as plt
plt.title("Actual derivative vs. estimate")
plt.plot(xs, actuals, 'rx', label = 'Actuals')
plt.plot(xs, estimates, 'b+', label = "Estimates")
plt.legend(loc=9)
plt.show()

###########################################################

def gradient_step(v: Vector, gradient: Vector, step_size: float)->Vector:
    """Moves 'step size' in the 'gradient' direction from 'v'"""
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)

def sum_of_squares_gradient(v: Vector)->Vector:
    return [2*v_i for v_i in v]

#Pick random starting point
v = [random.uniform(-10, 10) for i in range(3)]

for epoch in range(1000):
    grad = sum_of_squares_gradient(v)
    v = gradient_step(v, grad, -0.01)
    print(epoch, v)

assert distance(v, [0, 0, 0]) < 0.001
