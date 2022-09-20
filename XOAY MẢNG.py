dem = int(input())
while (dem):
    dem -= 1
    [n, d] = [int(o) for o in input().strip().split(' ', 2)]
    li = [int(o) for o in input().strip().split(' ', n)]
    s = ''
    for i in range(d, len(li)):
        s += str(li[i])+' '
    for i in range(0, d):
        s += str(li[i])+' '
    print(s)