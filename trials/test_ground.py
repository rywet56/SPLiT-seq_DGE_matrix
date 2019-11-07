import os
import psutil
process = psutil.Process(os.getpid())
print("The memory usage was: " + str(process.memory_info().rss/1000000000) + " GB")  # in bytes

test = []
for number in range(1,4000000):
    test.append(number)

# print(test)

process = psutil.Process(os.getpid())
print("The memory usage was: " + str(process.memory_info().rss/1000000000) + " GB")  # in bytes