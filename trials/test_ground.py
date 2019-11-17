import os
import psutil
# process = psutil.Process(os.getpid())
# print("The memory usage was: " + str(process.memory_info().rss/1000000000) + " GB")  # in bytes
#
# test = []
# for number in range(1,4000000):
#     test.append(number)
#
# # print(test)
#
# process = psutil.Process(os.getpid())
# print("The memory usage was: " + str(process.memory_info().rss/1000000000) + " GB")  # in bytes



import numpy as np
import gc
import sys
from scipy.sparse import csr_matrix
A = [[1, 0, 0, 1, 0, 0], [0, 0, 2, 0, 0, 1], [0, 0, 0, 2, 0, 0]]
S = csr_matrix(A)
print(sys.getsizeof(A))
print(sys.getsizeof(S))
del A
process = psutil.Process(os.getpid())
print("The memory usage was: " + str(process.memory_info().rss/1000000000) + " GB")
