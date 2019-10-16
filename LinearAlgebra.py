from typing import List, Tuple
import math

Vector = List[float]
Matrix = List[List[float]]

def add(v: Vector, w: Vector)->Vector:
    """Add corresponding elements"""
    assert len(v) == len(w), "Vectors must be the same dimension"
    return [v_i+w_i for v_i, w_i in zip(v, w)]

def substract(v: Vector, w: Vector)->Vector:
    """Substract corresponding elements"""
    assert len(v) == len(w), "Vectors must be the same dimentsion"
    return [v_i-w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors: List[Vector])->Vector:
    """Sum all corresponding elements"""
    assert vectors, "No vectors provided"
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Different vector dimensions"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

def scalar_multiply(c: float, v: Vector)->Vector:
    """"Multiplies every elements by c"""
    return [c*v_i for v_i in v]

def vector_mean(vectors: List[Vector])->Vector:
    """Compute the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v: Vector, w: Vector)->float:
    """Computes the dot product of two vectors"""
    assert len(v) == len(w), "Vectors must have the same dimensions"
    return sum(v_i*w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v: Vector)->float:
    return dot(v, v)

def magnitude(v: Vector)->float:
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector)->float:
    return sum_of_squares(substract(v, w))

def distance(v: Vector, w: Vector)->float:
    return math.sqrt(squared_distance(v, w))

def shape(A: Matrix)->Tuple[int, int]:
    """Return (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A: Matrix, i: int)->Vector:
    """Return the i-th row of matrix A as a vector"""
    return A[i]

def get_column(A: Matrix, j: int)->Vector:
    """Return the j-th column of matrix A as a vector"""
    return [A_i[j] for A_i in A]

############################################################

from typing import Callable

def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float])->Matrix:
    """Returns a num_rows x num_cols matrix whose (i, j)-th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

def indentity_matrix(n: int)->Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert indentity_matrix(5) == [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
