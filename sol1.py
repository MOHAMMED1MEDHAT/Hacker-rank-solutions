

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    dist_apl,dist_org=[],[]
    num_apl_hit,num_org_hit=0,0
    for i in apples:
        dist_apl.append(a+i)
    for i in oranges:
        dist_org.append(b+i)
    for x in dist_apl:
        if x>=s  or(x<=t and x>=s):
            num_apl_hit=num_apl_hit+1
    for y in dist_org:
        if (y>=s and y<=t) or y<=t  :
            num_org_hit=num_org_hit+1
    
    return f"{num_apl_hit}\n{num_org_hit}"         

      
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    print(countApplesAndOranges(s, t, a, b, apples, oranges))
