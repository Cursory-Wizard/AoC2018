import time
from datetime import timedelta

start_time = time.monotonic()
untouched = {}
pattern = {}
patternSizes = {}
with open("freq3.txt", "r") as f:
    content = f.readlines()
    for lines in content:
        strp2 = lines.split(" @ ")
        strp3 = strp2[1].split(": ")
        strp4 = strp3[0].split(",")
        strp5 = strp3[1].split("x")

        prelocX=strp4[0].strip()
        prelocY=strp4[1].strip()
        premotionX = strp5[0].strip()
        premotionY =strp5[1].strip()
        locationX = int(prelocX)
        locationY = int(prelocY)
        motionX = int(premotionX)
        motionY = int(premotionY)

        patt = motionX*motionY
        patternSizes[strp2[0]] = patt

        for i in range(locationX + 1, locationX + motionX + 1, 1):
            for j in range(locationY + 1, locationY + motionY + 1, 1):
                key = str(i) + "x" + str(j)
                if key not in pattern:
                    pattern[key] = [strp2[0]]
                else:
                    pattern[key].append(strp2[0])

    overlap = 0
    for key in pattern:
        if len(pattern[key]) > 1:
            overlap += 1
    print(overlap)

    for key in pattern:
        if len(pattern[key]) == 1:
            newkey = str(pattern[key])
            if newkey not in untouched:
                untouched[newkey] = 1
            else:
                untouched[newkey] += 1

    for key in untouched:
        secondKey = str(key).strip("['")
        thirdKey = secondKey.strip("']")

        if untouched[key] == patternSizes[thirdKey]:
            print(key)
            break



    end_time = time.monotonic()
    print(timedelta(seconds=end_time - start_time))