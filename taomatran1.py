n = int(input())

MAX = int(n / 2)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i <= MAX):
            if (j <= MAX): print(j, end=' ')
            else: print('0', end=' ')
        else:
            if (j > MAX): print(n-j+1, end=' ')
            else: print('0', end=' ')
    print()
