import time

print(time.time())

sum = 0
for i in range(1000000):
    sum += 1

print(time.time())