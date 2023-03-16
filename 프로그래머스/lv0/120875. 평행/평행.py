def solution(dots):
    answer = 0
    # 노가다 문제
    def calc(p1, p2):
        return (p2[1] - p1[1]) / (p1[0] - p2[0])
    if calc(dots[0], dots[1]) == calc(dots[2], dots[3]):
        return 1
    if calc(dots[0], dots[2]) == calc(dots[1], dots[3]):
        return 1
    if calc(dots[0], dots[3]) == calc(dots[1], dots[2]):
        return 1
    return 0