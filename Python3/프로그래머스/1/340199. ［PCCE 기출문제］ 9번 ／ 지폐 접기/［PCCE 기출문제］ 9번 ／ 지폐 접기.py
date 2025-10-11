def solution(wallet, bill):
    cnt = 0
    while max(bill) > max(wallet) or  min(bill) > min(wallet) :
        if bill[0] > bill[1]:
            bill[0] =bill[0] // 2
            cnt += 1
        else :
            bill[1] = bill[1] // 2
            cnt += 1
            
    return cnt