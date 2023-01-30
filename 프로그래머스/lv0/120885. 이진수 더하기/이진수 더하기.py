def solution(bin1, bin2):
    deci1 = int(bin1, 2)
    deci2 = int(bin2, 2)
    return str(bin(deci1 + deci2))[2:]