def solution(n):
    li = []
    answer = 0
    while n>0:
        li.append(n % 3) #리스트로 처리하고 하니까 자동으로 뒤집어진 게 됨!
        n //= 3
    for i in range(len(li)):
        answer += li[i] *(3**(len(li)-1-i))
    return answer