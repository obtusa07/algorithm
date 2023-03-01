while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    top = max(a, b, c)
    if top == a:
        if b**2 + c**2 == a**2:
            print("right")
        else:
            print("wrong")
    if top == b:
        if c**2 + a**2 == b**2:
            print("right")
        else:
            print("wrong")
    if top == c:
        if a**2 + b**2 == c**2:
            print("right")
        else:
            print("wrong")
