from math import isqrt
def solution(number, limit, power):
    total = 0
    for i in range (1, number +1):
        cnt = 0
        r = isqrt(i)
        for j in range(1, r+1):
            if i % j == 0:
                cnt += 1 if j * j == i else 2
        total += cnt if cnt <= limit else power
    return total