import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    counts = [0] * k
    for i in S:
        counts[i % k] += 1
    
    # If there are more than 1 numbers divisible by k, you can only pick 1 of them
    count = min(counts[0], 1)
    
    for i in range(1, (k//2)+1):
        if i != k - i:
            count += max(counts[i], counts[k-i])
    if k % 2 == 0 and counts[k % 2] > 0: 
        count += 1
    print(count)

nk = input().split()
n = int(nk[0])
k = int(nk[1])
S = list(map(int, input().rstrip().split()))
nonDivisibleSubset(k, S)