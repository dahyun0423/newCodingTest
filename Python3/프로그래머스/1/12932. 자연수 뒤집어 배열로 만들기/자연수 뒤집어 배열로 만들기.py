def solution(n):
    num = []
    num = map(int,str(n)[::-1])
    reserved_num = list(num)
    return reserved_num