def solution(sizes):
    # 사고과정 정리
    # 최댓값을 명함의 가로에 둘거고 2차원 배열로 뒀을 대 0열에
    # 최솟값들을 명함의 세로에 둘것, 2차월 배열에선 1열에
    widths = [max(w, h) for w, h in sizes]
    heights = [min(w, h) for w, h in sizes]
    area = max(widths) * max(heights)
    return area