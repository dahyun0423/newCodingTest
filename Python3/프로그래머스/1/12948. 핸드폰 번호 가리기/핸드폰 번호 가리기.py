def solution(phone_number):
    #얘 슬라이싱 기법 쓰면 될것같은데
    #마지막기준 4칸 앞만 보여주고 그 앞에는 *로 도배
    first = "*" * (len(phone_number) - 4)
    last = phone_number[-4:] 
    return first+last