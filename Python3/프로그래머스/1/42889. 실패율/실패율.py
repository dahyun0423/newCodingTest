def solution(N, stages):
    # 각 스테이지 번호에 머물러있는 인원 먼저 카운트 하시고 counts[1] = 1
    counts = [0] * (N +2) #(1~N+1)범위먼저
    for s in stages:
        counts[s] += 1 
        
        # 2) 실패율 계산
        alive = len(stages)  # 현재 스테이지에 도달은 한 인원 => 분모
        fails = []
        
    for i in range(1, N+1):
        stuck = counts[i] #분자
        reached = alive #분모
        fail = stuck / reached if reached != 0 else 0.0
        fails.append((i,fail))
        alive -= stuck
    
    ranking = sorted(fails, key=lambda x: (-x[1], x[0]))
    return [stage for stage, _ in ranking]
                