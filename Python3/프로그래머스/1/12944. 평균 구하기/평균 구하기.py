def solution(arr):
    avg = 0
    sum = 0
    for i in arr:
        sum += i
        avg = sum / len(arr)
    return avg