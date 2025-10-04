def solution(s):
    #공백기준으로 단어들을 나누었고
    splitS = s.split(' ') 
    #각 단어에 접근해 짝수 홀수 구분
    result = []
    for word in splitS:
        newWord = ""
        for i, ch in enumerate(word):
            if i % 2 ==0:
                newWord += ch.upper()
            else:
                newWord += ch.lower()
        result.append(newWord)
    #다시 .join으로 붙여야해
    return " ".join(result)
    