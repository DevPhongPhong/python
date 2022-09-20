import math


def CheckPrime(x):
    if x <= 1:
        return 0
    if x <= 3:
        return 1
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return 0
    return 1


def CheckDX(x):
    x = str(x)
    length = len(x)
    for i in range(0, int(length/2)+1):
        if (x[i] != x[length-1-i]):
            return 1
    return 0
