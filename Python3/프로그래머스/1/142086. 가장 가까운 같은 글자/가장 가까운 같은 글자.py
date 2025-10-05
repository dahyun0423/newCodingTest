def solution(s):
    # 해당 문자를 본적이 있는지를 확인해야하는데
    # 있어? 그러면 현재 위치와의 거리 = 현재 인덱스 - 마지막 인덱스
    result = [] # 각 문자 거리 저장
    last = {}  #문자의 마지막 인덱스 저장
    map = dict()
    for i in range(len(s)) :
        ch = s[i]
        
        if ch not in last:
            result.append(-1)
        else:
            result.append(i - last[ch])
        last[ch] = i
    return result