def solution(t, p):
    count = 0
    for i in range(len(t)-len(p)+1):
        num = t[i:i+len(p)]
        if(int(num)<= int(p)):
            count +=1
    return count