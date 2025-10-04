def solution(number):
    #세개의 합이 0인 것들을 넣어야해 count +1 증가시켜
    count = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if (number[i]+ number[j]+number[k] == 0):
                    count += 1
    return count