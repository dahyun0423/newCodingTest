def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        #약수의 개수가 짝수인 수는 더해
        count = 0
        for j in range(1,i+1):
            if i % j ==0:
                count += 1
        if(count %2 ==0):
            answer += i
        #홀수인 수는 뺀 수를!
        else :
            answer -= i
    return answer