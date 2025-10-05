def solution(s, n):
    result = ''
    #아스키코드로 풀거고
    for ch in s:
        if ch == ' ':
            result += ' '
            continue
        if 'A' <= ch <= 'Z' :
            result += chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        elif 'a' <= ch <= 'z' :
            result += chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
    return result