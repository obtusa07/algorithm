def solution(angle):
    if angle == 180:
        return 4
    if 90 < angle < 180:
        return 3
    if 90 == angle:
        return 2
    return 1