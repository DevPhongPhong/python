import json
import os
import msvcrt


def lineToDict(line):
    return {
        "Date": line[0:10:1].strip(),
        "Time": line[11:19:1].strip(),
        "Attr": line[20:25:1].strip(),
        "Size": line[26:39:1].strip(),
        "Compressed": line[40:52:1].strip(),
        "Name": line[53::1].strip()
    }


def createOrModifyFolderAndFile(MSV, prefixOfFile):
    fileName = '\\' + MSV + '\\' + prefixOfFile + ".txt"

    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    count = 1
    checkExist = 0
    for path in os.listdir('\\' + MSV):
        if (path == (prefixOfFile + '.txt')):
            checkExist = 1
            break
        if os.path.isfile(os.path.join('\\' + MSV, path)):
            count += 1
    if not checkExist:
        with open(fileName, "a") as f:
            f.write(str(count) + " ")


#---------------------------------------------------------------------------------------
while True:
    print("Copy data file to C:\\")
    print('Type "start" to start')
    if input() == "start":
        break
try:
    msvcrt.getch()

    file_to_read = '\\' + 'G18LogAllDownload202210142034ForProcess.txt'
    file_to_write = '\\' + 'reportSample.txt'
    End = "------------------- ----- ------------ ------------  ------------------------"
    listStudentCode = []
    listStudentDict = []

    with open(file_to_read) as fileRead:

        studentDict = {}
        checkData = False

        for line in fileRead:
            s = line.rstrip()

            if s == End:
                checkData = not checkData
                continue

            if checkData:
                record = lineToDict(s)
                record_name = record["Name"].split("\\")

                MSV = record_name[0]
                FileName = record_name[-1]
                endOfFile = FileName[-1:-5:-1][::-1]
                prefixOfFile = ""

                checkWavTxt = 0
                if endOfFile == '.wav':
                    checkWavTxt = 1
                    prefixOfFile = FileName.split("-")[0]
                elif endOfFile == '.txt':
                    checkWavTxt = 2
                    prefixOfFile = FileName.split("-")[0]
                else:
                    checkWavTxt = 0

                if prefixOfFile != "":
                    createOrModifyFolderAndFile(MSV, prefixOfFile)

                if MSV not in listStudentCode:
                    listStudentCode.append(MSV)
                    studentDict[MSV] = {
                        "nWavFile": (1 if checkWavTxt == 1 else 0),
                        "nTxtFile": (1 if checkWavTxt == 2 else 0),
                    }
                else:
                    studentDict[MSV] = {
                        "nWavFile":
                        (studentDict[MSV]["nWavFile"] +
                        1 if checkWavTxt == 1 else studentDict[MSV]["nWavFile"]),
                        "nTxtFile":
                        (studentDict[MSV]["nTxtFile"] +
                        1 if checkWavTxt == 2 else studentDict[MSV]["nTxtFile"]),
                    }

    print('\nDanh Sach Sinh Vien:')
    for i in listStudentCode:
        print(i)
        listStudentDict.append({i: studentDict[i]})

    with open("\listStudentDict.json", "w+") as f:
        f.write(json.dumps(listStudentDict))

    while (True):
        print('\nType "end" to end')
        if input() == "end":
            break
except:
    print("Error! Press key to end")
    msvcrt.getch()
    