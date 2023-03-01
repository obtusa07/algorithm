x, y, w, h = map(int, input().split())
result = 1001
result = min(abs(x), result)
result = min(abs(y), result)
result = min(abs(w - x), result)
result = min(abs(h - y), result)
print(result)