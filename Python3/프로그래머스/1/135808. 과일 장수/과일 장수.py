def solution(k, m, score):
    # 거꾸로 정렬을 먼저 해
    score.sort(reverse=True)
    
    total = 0
    for i in range(len(score)//m):
        #최저의 값으로 박스 수 구해야해
        mini = score[(i+1) * m -1]
        total += mini * m
    return total
