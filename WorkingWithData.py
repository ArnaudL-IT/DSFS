from typing import List, Dict
from collections import Counter
import math

import matplotlib.pyplot as plt

def bucketize(point: float, bucket_size: float)->float:
    """Floor the point to the next lower multiple of bucket_size"""
    return bucket_size ** math.floor(point / bucket_size)
