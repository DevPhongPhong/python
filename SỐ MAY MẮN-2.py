x = int(input())
while (x):
    x -= 1
    n = input()
    b = "YES"
    for c in n:
        if c != '4' and c != '7':
            b = "NO"
            break
    print(b)
