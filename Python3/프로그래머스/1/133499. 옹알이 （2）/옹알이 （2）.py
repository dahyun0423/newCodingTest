def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    for word in babbling:
        for sound in baby:
            if sound * 2 in word : #연속발음 불가
                break
            word = word.replace(sound, " ") #발음 가능한 부분을 공백처리
        else : #연속되는 발음 없으면
            if word.strip() == "":#모든 발음 제거했을때 발음 가능한 단어
                cnt+=1
    return cnt