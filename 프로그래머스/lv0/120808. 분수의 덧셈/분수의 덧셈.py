import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    gcd_denoms = math.gcd(denom1, denom2)
    new_lcm = denom1*denom2 // gcd_denoms
    new_numer = int(numer1 * (new_lcm / denom1) + numer2 * (new_lcm / denom2))
    
    gcd = math.gcd(new_numer, new_lcm)
    return [new_numer/gcd, new_lcm/gcd]