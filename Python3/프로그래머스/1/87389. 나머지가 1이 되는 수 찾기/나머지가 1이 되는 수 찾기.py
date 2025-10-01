def solution(n):
    #나머지가 1이여야한다
    # n = q * x + 1
    # n - 1 = q * x -> x는 n-1의 약수 중 하나여야만해.
    for x in range(2, n) : 
        if n % x == 1:
            return x
    
            