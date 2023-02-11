def solution(keyinput, board):
    answer = [0, 0]
    for key in keyinput:
        if key == 'up' and answer[1] < (board[1] // 2):
            answer[1] += 1
        elif key == 'down' and answer[1] > -(board[1] // 2):
            answer[1] -= 1
        elif key == 'left' and answer[0] > -(board[0] // 2):
            answer[0] -= 1
        elif key == 'right' and answer[0] < board[0] // 2:
            answer[0] += 1
    return answer