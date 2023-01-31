def solution(id_pw, db):
    for candidates in db:
        if candidates[0] == id_pw[0]:
            if candidates[1] == id_pw[1]:
                return "login"
            return "wrong pw"
    return "fail"