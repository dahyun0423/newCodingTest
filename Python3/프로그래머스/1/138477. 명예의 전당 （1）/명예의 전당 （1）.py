import heapq
def solution(k, score):
    honor = []
    answer = []
    
    for i in score:
        heapq.heappush(honor, i)
        if(len(honor) > k):
            heapq.heappop(honor)
        answer.append(honor[0])
    return answer
    