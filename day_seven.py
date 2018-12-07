
import time
from datetime import timedelta
start_time = time.monotonic()

alphalist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
opening = []
instruct = {}
with open("freq7.txt", "r") as f:
    content = f.readlines()
    for lines in content:
        redux = lines.split()
        opening.append([redux[1], redux[7]])
    print(opening)
    for pair in opening:
        if pair[1] in instruct:
            value = instruct[pair[1]]
            print(value)
            instruct[pair[1]] = value + pair[0]
        else:
            instruct[pair[1]] = pair[0]
            alphalist = alphalist.replace(pair[1], "")
    print(instruct)
    print(alphalist)
    on_order = instruct.copy()
    in_queue = alphalist


    master = []
    rolling = True
    while rolling:
            letter = alphalist[0]
            master.append(letter)
            alphalist = alphalist[1:]
            for key in instruct:
                testphrase = instruct[key]
                if letter in testphrase:
                    testphrase = testphrase.replace(letter, "")
                    if len(testphrase) == 0:
                        alphalist += key
                        beta = sorted(alphalist)
                        alphalist = beta
                    instruct[key] = testphrase
            if len(alphalist) == 0:
                rolling = False
    answer = ""
    for letter in master:
        answer += letter
    print(answer)


    totaltime = 0
    chargelist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    being_worked = {}
    completed = []
    workers = 5
    rolling = True
    while rolling:
        # assign workers while we have workers and jobs
        while workers > 0 and len(in_queue) > 0:
            letter = in_queue[0]
            in_queue = in_queue[1:]
            worktime = chargelist.find(letter) + 61
            being_worked[letter] = [0, worktime]
            workers -= 1
        #increment each job timer
        for job in being_worked:
            being_worked[job][0] += 1
            if being_worked[job][0] == being_worked[job][1]:
                completed.append(job)
                workers += 1
        for job in completed:
            del being_worked[job]
        totaltime += 1
        # check if job is done and if this opens new job.
        for letter in completed:
            for key in on_order:
                testphrase = on_order[key]
                if letter in testphrase:
                    testphrase = testphrase.replace(letter, "")
                    if len(testphrase) == 0:
                        in_queue += key
                        beta = sorted(in_queue)
                        in_queue = beta
                    on_order[key] = testphrase
            completed.remove(letter)
        if len(completed) == 0 and len(being_worked) == 0 and len(in_queue) == 0:
            rolling = False
    print(totaltime)

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))