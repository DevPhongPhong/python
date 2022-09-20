import math

dem = int(input())

def CheckPrime(x):
    if x <= 1:
        return 0
    if x <= 3:
        return 1
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return 0
    return 1


while (dem):
    dem -= 1
    n = int(input())
    li = []
    count = 0
    for i in range(1, n+1):
        if (CheckPrime(i)):
            li.append(i)
    for i in range(0, len(li)-3+1):
        if (li[i+1] == li[i]+2 and li[i+2] == li[i]+6) or (li[i+1] == li[i]+4 and li[i+2] == li[i]+6):
            count += 1
    print(count)