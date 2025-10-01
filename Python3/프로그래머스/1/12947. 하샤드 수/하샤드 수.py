def solution(x):
    # <사고방식 정리>
    # 자리수를 구하는게 먼저
    # 각 자리수를 더하고
    # x 가 각 자리수의 합에 나누어 떨어지면 하샤드 수 =>True
    # 안나눠떨어지면 => false
    original = x
    total = 0
    while x > 0:
        digit = x % 10 # 마지막 자리수
        x //= 10 #한 자리 줄이기
        total += digit
    
    if(original % total == 0):
        return True
    else:
        return False