from re import L


n=int(input())
while n:
    n-=1
    s=[list(x) for x in input().split(" ")]
    s[0].sort()
    s[1].sort()
    print(s[1]==s[0])
    