def solution(a, b, n):
    total = 0
    while n >= a:
        exchange = (n // a) * b
        total += (n // a) * b
        n = (n % a) + exchange
    return total