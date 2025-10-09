def solution(name, yearning, photo):
    answer = []
    score = dict(zip(name, yearning))
    for person in photo:
        total = sum(score.get(p,0) for p in person)
        answer.append(total)
    return answer