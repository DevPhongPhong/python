def FindMin(l):
    Min = l[0]
    for c in l:
        if c < Min:
            Min = c
    return Min
def FindNumber(str):
    l = []
    strTemp = ""
    for c in str:
        if ord(c) >= 48 and ord(c) <= 57:
            strTemp += c
        else:
            if strTemp != "":
                l.append(int(strTemp))
            strTemp = ""
    if strTemp != "":
        l.append(int(strTemp))

    return l

n = int(input())
i = 0
ls = []

while i < n:
    ls.append(input())
    i += 1

i = 0
while i < n:
    print(FindMin(FindNumber(ls[i])))
    i+=1