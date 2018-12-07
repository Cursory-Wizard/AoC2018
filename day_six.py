import urllib
import time
from datetime import timedelta
start_time = time.monotonic()

def iterator(xmin, ymin, xmax, ymax, step, dealwithevens, dictmatch):
    dictList = {}
    listList = []
    possibleEven = False
    for y in range(1, 400, 1):
        for x in range(1, 400, 1):
            distXY = ["0x0", 1000]
            for raypoint in totallist:
                driveX = raypoint[0] - x
                driveY = raypoint[1] - y
                if driveX < 0:
                    driveX *= -1
                if driveY < 0:
                    driveY *= -1
                totalDrive = driveX + driveY
                if totalDrive == distXY[1]:
                    possibleEven = True
                if totalDrive < distXY[1]:
                    distXY[1] = totalDrive
                    distXY[0] = str(raypoint[0]) + "x" + str(raypoint[1])
                    possibleEven = False
            if possibleEven and dealwithevens:
                distXY[0] = "*x*"
                possibleEven = False
            key = distXY[0]
            if dictmatch:
                if key not in dictList:
                    dictList[key] = 1
                else:
                    dictList[key] += 1
            else:
                if distXY[0] not in listList:
                    listList.append(distXY[0])
    if dictmatch:
        return dictList
    else:
        return listList

with open("freq6.txt", "r") as f:
    content = f.readlines()
    totallist = []
    for line in content:
        coords = line.split(", ")
        totallist.append([int(coords[0]), int(coords[1])])


    dangerList = {}
    dangerList = iterator(1, 1, 400, 400, 1, True, True)
    # possibleEven = False
    # for y in range(1, 400, 1):
    #     for x in range(1, 400, 1):
    #         distXY = ["0x0", 1000]
    #         for raypoint in totallist:
    #             driveX = raypoint[0] - x
    #             driveY = raypoint[1] - y
    #             if driveX < 0:
    #                 driveX *= -1
    #             if driveY < 0:
    #                 driveY *= -1
    #             totalDrive = driveX + driveY
    #             if totalDrive == distXY[1]:
    #                 possibleEven = True
    #             if totalDrive < distXY[1]:
    #                 distXY[1] = totalDrive
    #                 distXY[0] = str(raypoint[0]) + "x" + str(raypoint[1])
    #                 possibleEven = False
    #         if possibleEven:
    #             distXY[0] = "*x*"
    #             possibleEven = False
    #         key = distXY[0]
    #         if key not in dangerList:
    #             dangerList[key] = 1
    #         else:
    #             dangerList[key] += 1
    # print(dangerList)
    exclusionList = []
    for x in range(0,401):
        for y in range(0,402,400):
            distXY = [[0, 0], 1000]
            for raypoint in totallist:
                driveX = raypoint[0] - x
                driveY = raypoint[1] - y
                if driveX < 0:
                    driveX *= -1
                if driveY < 0:
                    driveY *= -1
                totalDrive = driveX + driveY
                if totalDrive == distXY[1]:
                    possibleEven = True
                if totalDrive < distXY[1]:
                    distXY[1] = totalDrive
                    distXY[0] = [raypoint[0], raypoint[1]]
                    possibleEven = False
            if possibleEven:
                distXY[0] = [0, 0]
            else:
                if distXY[0] not in exclusionList:
                    exclusionList.append(distXY[0])
    for x in range(0, 402, 400):
        for y in range(0, 401, 1):
            distXY = [[0, 0], 1000]
            for raypoint in totallist:
                driveX = raypoint[0] - x
                driveY = raypoint[1] - y
                if driveX < 0:
                    driveX *= -1
                if driveY < 0:
                    driveY *= -1
                totalDrive = driveX + driveY
                if totalDrive == distXY[1]:
                    possibleEven = True
                if totalDrive < distXY[1]:
                    distXY[1] = totalDrive
                    distXY[0] = [raypoint[0], raypoint[1]]
                    possibleEven = False
            if possibleEven:
                distXY[0] = [0, 0]
            else:
                if distXY[0] not in exclusionList:
                    exclusionList.append(distXY[0])


    for pair in exclusionList:
        key = str(pair[0]) + "x" + str(pair[1])
        del dangerList[key]
    print(dangerList)
    safeList = 0
    for x in range(0, 402, 1):
        for y in range(0, 401, 1):
            distXY = 0
            for raypoint in totallist:
                driveX = raypoint[0] - x
                driveY = raypoint[1] - y
                totalDrive = abs(driveX) + abs(driveY)
                distXY += totalDrive
            if distXY < 10000:
                safeList += 1

    print(safeList)
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))