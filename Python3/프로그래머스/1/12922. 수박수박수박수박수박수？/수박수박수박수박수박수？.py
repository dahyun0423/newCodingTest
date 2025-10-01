def solution(n):
    #사고를 해보자.
    #수박이라는 글자를 쪼개서 담아서 반복을 해야하는게 좋은 것같음
    #짝수면 수박 수박수박 수박수박 홀수면 수 수박수 수박수박수 
    #홀수는 뒤에 수만 한번더 붙이면 된다.
    check = n // 2
    if n % 2== 0 : 
        return "수박" * check
    else :
        return "수박" *check + "수"