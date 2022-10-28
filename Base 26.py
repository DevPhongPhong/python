def convertTo10(l):
    res = 0
    for c in l:
        res = res * 26 + (ord(c) - 97)
    return res


def convertTo26(num):
    if num < 0:
        return ""
    elif num < 26:
        return chr(97 + num)
    else:
        return convertTo26(int(num / 26)) + chr(97 + num % 26)



# print(convertTo26(0))
# print(convertTo26(1))
# print(convertTo26(2))
# print(convertTo26(25))
# print(convertTo26(26))
# print(convertTo26(27))
# print(convertTo26(52))

n = int(input())
while n:
    n -= 1
    s = [list(x) for x in input().split()]
    print(convertTo26(convertTo10(s[0]) + convertTo10(s[1])))