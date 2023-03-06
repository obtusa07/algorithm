def solution(wallpaper):
    start_x, start_y, end_x, end_y = len(wallpaper), len(wallpaper[0]), 0, 0
    print([start_x, start_y, end_x, end_y])
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                start_x = min(start_x, i)
                start_y = min(start_y, j)
                end_x = max(end_x, i)
                end_y = max(end_y, j)
    return [start_x, start_y, end_x+1, end_y+1]
