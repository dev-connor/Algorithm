import math

def getLcm(a, b):
    return a * b / math.gcd(a, b)
def solution(numer1, denom1, numer2, denom2):
    lcm = getLcm(denom1, denom2)
    numer1 = numer1 * (lcm / denom1)
    numer2 = numer2 * (lcm / denom2)
    numer3 = numer1 + numer2

    gcd = math.gcd(int(numer3), int(lcm))

    if gcd == 1:
        return [int(numer3), int(lcm)]
    else:
        return [int(numer3 / gcd), int(lcm / gcd)]

if __name__ == '__main__':
    # result = solution([1,2,3])
    result = solution(1,2,3,4)
    print(result)

