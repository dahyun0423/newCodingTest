def solution(arr):
    mini = min(arr) #이걸 미리 안하고 컴프리헨션 안에다가 넣으면 매번 다시 호출해서 시간초과 뜨기에 비효율적인 게 됨. 그래서 미리 선언하세요!
    answer = [i for i in arr if i != mini]
    if not answer:
        return [-1]
    
    return answer