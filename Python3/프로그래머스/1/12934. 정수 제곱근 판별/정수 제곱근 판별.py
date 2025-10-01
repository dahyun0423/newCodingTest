def solution(n):
    #n이 x의 제곱인지 판단하는 문제
    #n이 x의 제곱이라면 x+1의 제곱을 리턴 , -1
    x = n ** 0.5
    if x.is_integer():
        return int(x+1)**2
    else:
        return -1