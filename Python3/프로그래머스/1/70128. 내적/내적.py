
def solution(a, b):
    k = []
    for i in range(len(a)):
        k.append(a[i] * b[i])
    return sum(k)