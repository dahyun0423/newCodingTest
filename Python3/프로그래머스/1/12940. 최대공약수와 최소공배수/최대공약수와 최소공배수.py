def solution(n, m):
    ln, lm, answer = [],[],[]
    
    #n의 약수
    for i in range(1,n+1):
        if n % i == 0 : 
            ln.append(i)
            
    #m의 약수
    for j in range(1,m+1):
        if m % j == 0:
            lm.append(j)
    
    #최대공약수
    temp = set(ln) & set(lm)
    g = max(temp)
    
    #최소공배수
    l = (n*m) //g
    
    answer.append(g)
    answer.append(l)
    
    return answer