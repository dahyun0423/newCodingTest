from itertools import *
import math 

def solution(nums):
    
    printList = list(combinations(nums, 3))
    
    sums = [a+b+c for (a,b,c)in printList]
    
    count = 0
    for s in sums:
        if is_prime(s):
            count += 1

    return count 

def is_prime(sums):
    if sums < 2:
        return False
    for i in range(2,int(math.sqrt(sums))+1):
        if sums % i == 0:
            return False
    return True
            
            