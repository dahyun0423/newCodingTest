def solution(a, b):
    start = min(a,b)
    end = max(a,b)
    
    #항의 개수
    n = end - start + 1
    
    #등차수열의 합공식
    return n*(start+end) //2