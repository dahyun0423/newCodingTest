def solution(price, money, count):
    #본 이용료 price
    #count : 몇 번 타는지: n번 이용하면 price *n
    #money : 내돈일세
    #요거 시그마 문제군
    #price + price*i 
    for i in range(1, count+1):
        money -= price * i
    return 0 if money >= 0 else abs(money)