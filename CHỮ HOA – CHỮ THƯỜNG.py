s = input()
countD = 0
countU = 0
for c in s:
    if c <= 'Z' and c >= 'A':
        countU += 1
    else:
        countD += 1
print(s.lower() if countD>=countU else s.upper())
