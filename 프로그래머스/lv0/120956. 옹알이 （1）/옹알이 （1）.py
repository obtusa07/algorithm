def solution(babbling):
    speakable = ["aya", "ye", "woo", "ma"]
    answer = 0
    for word in babbling:
        for speak in speakable:
            word = word.replace(speak, "A", 1)
        if word.isupper():
            answer += 1
    return answer