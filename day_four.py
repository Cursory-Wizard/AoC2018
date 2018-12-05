from operator import itemgetter
import time
from datetime import timedelta

start_time = time.monotonic()

sleepList = {}
sleepLister = {}
guardList = {}


def addGuardDict(key):
    if key not in guardList:
        guardList[key] = 1
    else:
        guardList[key] += 1


def addSleepDictionary(key):
    if key not in sleepLister:
        sleepLister[key] = 1
    else:
        sleepLister[key] += 1


def timer(guard, sleepH, sleepM, wakeH, wakeM):
    for i in range(sleepM, wakeM, 1):
        key = str(guard) + "/" + str(wakeH) + "/" + str(i)
        addSleepDictionary(key)
        sleepKey = str(guard)
        addGuardDict(sleepKey)
        hourKey = str(wakeH) + "/" + str(i)
        if sleepKey not in sleepList:
            sleepList[sleepKey] = {}
            sleepList[sleepKey][hourKey] = 1
        else:
            if hourKey not in sleepList[sleepKey]:
                sleepList[sleepKey][hourKey] = 1
            else:
                sleepList[sleepKey][hourKey] += 1


with open("freq4.txt", "r") as f:
    content = f.readlines()
    totalList = []
    for lines in content:
        strOne = lines.split("-")
        month = int(strOne[1])
        day = int(strOne[2][0:2])
        hour = int(strOne[2][3:5])
        minute = int(strOne[2][6:8])
        strTwo = lines.split("] ")
        totalList.append([month, day, hour, minute, strTwo[1]])

    totalList.sort(key=itemgetter(0, 1, 2, 3))

    sleepTracker = {}
    guard = 0
    sleepH = 0
    sleepM = 0
    wakeH = 0
    wakeM = 0
    for entry in totalList:

        if entry[4][0] == "G":
            words = entry[4].split()
            guard = int(words[1][1:])
        elif entry[4][0] == 'f':
            sleepH = entry[2]
            sleepM = entry[3]
        elif entry[4][0] == 'w':
            wakeH = entry[2]
            wakeM = entry[3]
            timer(guard, sleepH, sleepM, wakeH, wakeM)
            sleepH = 0
            sleepM = 0
            wakeH = 0
            wakeM = 0

    answerKey = max(guardList, key=guardList.get)
    answer = max(sleepList[answerKey], key=sleepList[answerKey].get).split("/")
    print(int(answerKey) * int(answer[1]))
    answerTwo = max(sleepLister, key=sleepLister.get).split("/")
    print(int(answerTwo[0]) * int(answerTwo[2]))

    end_time = time.monotonic()
    print(timedelta(seconds=end_time - start_time))