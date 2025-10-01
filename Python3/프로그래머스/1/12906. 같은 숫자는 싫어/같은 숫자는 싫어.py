def solution(arr):
    #연속적으로 나타나는 숫자를 어떻게 처리해?
    #연속 중복을 없애고 싶어? 그럼 현재 원소. 바로 이전에 남긴 원소만 비교하면 돼.
    #마지막 원소는 어케할껀데?
    #
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if(arr[i] != arr[i-1]):
            answer.append(arr[i])
    return answer