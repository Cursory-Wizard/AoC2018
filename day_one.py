import time
from datetime import timedelta

start_time = time.monotonic()

result = 0
with open("freq.txt", "r") as f:
    content = f.readlines()
    f.close()
    outcome = []
    doThis = True
    tries = 1
    while doThis:
        for line in content:
            if line[0:1] == "-":
                result = result - int(line[1:])
            else:
                result = result + int(line[1:])
            outcome.append(result)

            if outcome.count(result)>1:
                print(result)
                doThis = False
                break
        tries += 1

print(result)


end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))