import sys
import math
si = sys.stdin.readline
a, b = map(int, si().split())
gcd = math.gcd(a, b)
print(gcd)
lcm = int(a*b / gcd)
print(lcm)