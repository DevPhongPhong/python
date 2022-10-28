from math import gcd

n = int(input())
try:
    while n:
        n -= 1
        _max = 1
        s = [int(x) for x in input().split(" ")]
        for x in s:
            for y in s:
                if x != y:
                    temp = gcd(x, y)
                    if temp > _max: _max = temp
        print(_max)
except:
    print("")