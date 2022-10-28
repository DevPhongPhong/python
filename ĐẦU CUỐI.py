x = int(input())
while x:
    x -= 1
    n = input()
    print("YES" if (n[0] + n[1]) == (n[-2] + n[-1]) else "NO")

