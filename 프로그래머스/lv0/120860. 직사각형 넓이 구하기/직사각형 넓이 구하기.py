def solution(dots):
    answer = 0
    height = max(dots[0][1], dots[1][1], dots[2][1], dots[3][1]) - min(dots[0][1], dots[1][1], dots[2][1], dots[3][1])
    width = max(dots[0][0], dots[1][0], dots[2][0], dots[3][0]) - min(dots[0][0], dots[1][0], dots[2][0], dots[3][0])
    
    return width*height