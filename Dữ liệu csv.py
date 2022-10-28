def process(country, year):
    file_to_open = "DP_LIVE_16102022143222532.csv"

    sum = 0
    count = 0
    li = []

    with open(file_to_open) as file:
        file.readline()
        for line in file:
            temp = line.rstrip().split(",")
            temp[5] = temp[5][0:4:1]
            if temp[0] == country and temp[5] == year:
                sum += float(temp[6].replace('.', ''))
                count += 1
                print(line.rstrip())

    print(sum / count)


country = input()
year = input()
process(country=country, year=year)
