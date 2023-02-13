def solution(spell, dic):
    #set을 사용해보면
    for elem in dic:
        if set(spell) == set(elem).intersection(set(spell)):
            return 1
    return 2