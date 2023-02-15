import itertools

def solution(k, dungeons):
    answer = []
    # 순열을 생성하면 모든 경우의 수가 발생
    per_dungeons = itertools.permutations(dungeons)
    
    for dungeons in per_dungeons:
        temp_k = k
        cnt = 0
        for dungeon in dungeons:
            if temp_k < dungeon[0]:
                answer.append(cnt)
                break
            temp_k -= dungeon[1]
            cnt += 1
        if cnt == len(dungeons):
            answer.append(cnt)
    
    return max(answer)