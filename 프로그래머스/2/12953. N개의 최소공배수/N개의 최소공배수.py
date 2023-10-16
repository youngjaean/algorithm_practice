import math
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    # return reduce(lambda a, b: math.lcm(a, b), arr) 이거 하면 되는데... 

    return reduce(lambda a, b: lcm(a, b), arr)