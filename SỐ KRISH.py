c = {
    "0": 1,
    "1": 1,
    "2": 2,
    "3": 6,
    "4": 24,
    "5": 120,
    "6": 720,
    "7": 5040,
    "8": 40320,
    "9": 362880
}
count = int(input())

while count:
    count -= 1
    try:
        n = input()
        sum = 0
        for _c in n:
            sum += c[_c]
        print("Yes" if str(sum) == n else "No")
    except:
        print("Yes")