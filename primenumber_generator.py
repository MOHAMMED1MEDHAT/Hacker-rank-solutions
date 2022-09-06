from __future__ import generators
import math
from queue import PriorityQueue
def check(n):
    if n == 1:
        return False
          
        # from 1 to sqrt(n) 
    for x in range(2, (int)(math.sqrt(n))+1):
        if n % x == 0:
            return False 
    return True
def prime_generator(n):
    for i in range(2,n):
        if check(i):
            x=i
    return x

n=5000000000000000000000000000
print(prime_generator(n))