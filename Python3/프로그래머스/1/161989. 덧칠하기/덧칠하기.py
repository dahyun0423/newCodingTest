def solution(n, m, section):
    paintRoll = 0   #아직 아무값도 안덮인걸 의미하고 얘는 젤 오른쪽으로 이동시키기
    count = 0
    
    for i in section : 
        if i > paintRoll : #덮이지 않았으니 덮어야해
            count += 1
            paintRoll = i + m -1
    
    return count