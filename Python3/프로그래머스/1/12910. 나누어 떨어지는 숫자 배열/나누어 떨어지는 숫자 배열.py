def solution(arr, divisor):
     #사고방식 재정리
    #divisor로 나누어 떨어지는 값만 모으기 => 이렇게 해야 뒤에 안꼬인다..
    #그리고 만약 이 배열에 안들어와있으면 -1리턴하고 들어있으면 오름차순 정리하면끝.
    answer = [x for x in arr if x % divisor == 0 ]
    
    if not answer :
        return [-1]
    
    return sorted(answer)