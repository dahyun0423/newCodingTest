def solution(food):
    left = []
    for i in range(1, len(food)):
        li = food[i] // 2
        left.append(str(i)*li)
    left_str = ''.join(left)
    return left_str + "0" + left_str[::-1]