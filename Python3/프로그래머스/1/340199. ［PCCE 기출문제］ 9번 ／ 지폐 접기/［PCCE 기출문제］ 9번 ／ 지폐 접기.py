def solution(wallet, bill):
    cnt = 0
    wmin, wmax = sorted(wallet)  
    while True:
        bmin, bmax = sorted(bill)
        # 들어갈 수 있으면 종료
        if bmin <= wmin and bmax <= wmax:
            break
        
        # 긴 변을 반으로 접기
        if bill[0] > bill[1]:
            bill[0] //= 2
        else :
            bill[1] //= 2
        
        cnt += 1
            
    return cnt