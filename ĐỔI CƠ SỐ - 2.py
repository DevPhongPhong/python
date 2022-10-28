from traceback import print_tb

base4 = {"00": "0", "01": "1", "10": "2", "11": "3"}
base8 = {
    "000": "0",
    "001": "1",
    "010": "2",
    "011": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7"
}
base16 = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}


def convert(type, s):
    res = ''
    if type == 2:
        res = s
    elif type == 4:
        while len(s) % 2 != 0:
            s = "0" + s
        for i in range(len(s), 0, -2):
            temp = s[i - 2:i:1]
            res = base4[temp] + res
    elif type == 8:
        while len(s) % 3 != 0:
            s = "0" + s
        for i in range(len(s), 0, -3):
            temp = s[i - 3:i:1]
            res = base8[temp] + res
    elif type == 16:
        while len(s) % 4 != 0:
            s = "0" + s
        for i in range(len(s), 0, -4):
            temp = s[i - 4:i:1]
            res = base16[temp] + res
    return res


count = int(input())
while count:
    count -= 1
    type = int(input())
    s = input()
    print(convert(type, s))
