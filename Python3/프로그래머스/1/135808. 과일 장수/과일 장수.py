def solution(k, m, score):
    # 거꾸로 정렬을 먼저 해
    score.sort(reverse=True)
    
    total = 0
    for i in range(len(score)//m):
        next = score[(i+1) * m -1]
        total += next * m
    return total