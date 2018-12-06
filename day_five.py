from operator import itemgetter
import time
from datetime import timedelta

start_time = time.monotonic()

firstlist = []

with open("freq5.txt", "r") as f:
    while True:
        c = f.read(1)
        if not c:
            break
        else:
            firstlist.append(c)
biglist = firstlist.copy()
counter = 0
running = True
while running:
    j = 0
    k = len(biglist)
    while j < (k - 1):
        tester = biglist[j]
        follower = biglist[j + 1]
        if tester.lower() == follower.lower():
            if tester.isupper() and follower.islower():
                del biglist[j + 1]
                del biglist[j]
                j -= 2
                counter += 1
            elif tester.islower() and follower.isupper():
                del biglist[j + 1]
                del biglist[j]
                j -= 2
                counter += 1
        j += 1
        k = len(biglist)
    if counter > 0:
        counter = 0
    else:
        running = False
print(len(biglist))

lowestlist = []
polylist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in polylist:
    checklist = [l for l in biglist if (l.lower() != letter.lower())]
    counter = 0
    running = True
    while running:
        j = 0
        k = len(checklist)
        while j < (k - 1):
            tester = checklist[j]
            follower = checklist[j + 1]
            if tester.lower() == follower.lower():
                if tester.isupper() and follower.islower():
                    del checklist[j + 1]
                    del checklist[j]
                    j -= 2
                    counter += 1
                elif tester.islower() and follower.isupper():
                    del checklist[j + 1]
                    del checklist[j]
                    j -= 2
                    counter += 1
            j += 1
            k = len(checklist)
        if counter > 0:
            counter = 0
        else:
            running = False
    lowestlist.append(len(checklist))
answer2 = min(s for s in lowestlist)
print(answer2)















end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))