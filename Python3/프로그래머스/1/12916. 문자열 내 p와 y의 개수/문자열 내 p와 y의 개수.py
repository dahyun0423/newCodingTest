def solution(s):
    #p의 개수와 y의 개수를 담는 변수가 필요하겠고
    #모두 없으셔? 그럼 항상 true. 비교해 같아도 true
    #다르셔? 그럼 false
    s = s.lower()
    p = s.count('p') 
    y = s.count('y')
    if (p == y) : 
        return True

    else :
        return False