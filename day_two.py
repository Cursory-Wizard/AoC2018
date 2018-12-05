import time
from datetime import timedelta

start_time = time.monotonic()
result = 0
with open("freq2.txt", "r") as f:
    content = f.readlines()
    f.close()
    timestwo = 0
    timesthree = 0
    for words in content:
        twoCount = False
        threeCount = False
        for letters in words:
            if words.count(letters) == 2:
                if not twoCount:
                    timestwo += 1
                    twoCount = True
            if words.count(letters) == 3:
                if not threeCount:
                    timesthree += 1
                    threeCount = True
            if twoCount and threeCount:
                break
    result = timestwo * timesthree
    print(result)


with open("freq2.txt", "r") as f:
    content = f.readlines()
    f.close()
    answer = []
    for checkWord in content:
        for compareWord in content:
            answer = [i for i in range(0, len(checkWord)) if checkWord[i] != compareWord[i]]
            if len(answer) == 1:
                print(checkWord)
                print(compareWord)
                break
            else:
                answer = []

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))