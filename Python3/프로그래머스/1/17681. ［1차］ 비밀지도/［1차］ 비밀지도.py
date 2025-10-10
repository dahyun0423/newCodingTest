def solution(n, arr1, arr2):
    #2차원 배열을 먼저 생성한다 기본 디폴트 값은 0인겨 (허거덩쓴 이건 필요없어)
    # arr1과 arr2에있는 숫자들을 2진수로 변환한다
    #거기에서 0은 " ". 즉 공백을 의미하며 1은 "#" 벽을 의미한다.
    #arr1과 arr2를 겹쳐 그래서 1+1 도 1이고 1+0 = 1 0+0인 즉 공백인 것만 찐 공백인겨 -> 비트연산자
    #그렇게해서 "#####" 이런식으로 표현한 비밀지도 문자열 배열을 출력해야해
    
    result = []
    for i in range(n):
        merged = arr1[i] | arr2[i]
        bn = bin(merged)[2:].zfill(n)
        
        row = []
        for ch in bn:
            if ch == '1' :
                row.append("#")
            else:
                row.append(' ')
        result.append(''.join(row))
        
    return result