def solution(n):
    line = list(map(int,str(n)))
    line.sort(reverse=True)
    result = ''.join(map(str,line))
    return int(result)