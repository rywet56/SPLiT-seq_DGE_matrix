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



# import numpy as np
# import gc
# import sys
# from scipy.sparse import csr_matrix
# A = [[1, 0, 0, 1, 0, 0], [0, 0, 2, 0, 0, 1], [0, 0, 0, 2, 0, 0]]
# S = csr_matrix(A)
# print(sys.getsizeof(A))
# print(sys.getsizeof(S))
# del A
# process = psutil.Process(os.getpid())
# print("The memory usage was: " + str(process.memory_info().rss/1000000000) + " GB")
from tools.file_input_output import read_from_file

sam_file = read_from_file(input_file="/Users/manuel/Desktop/bowtie_strategy/star_aligned.sam", file_type="sam")

# test uniqueness
# read_names = []
# for read in sam_file:
#     read_names.append(read[1].split(".")[1])

# import numpy as np
#
# print(np.unique(read_names).size)

total = 0
have_both = 0
nh = 0
for read in sam_file:
    total += 1
    if read[0].get_tag("NH") == 0:
        nh += 1
        if read[0].has_tag("uT"):
            have_both += 1

print(have_both)
print(total)


# print(len(sam_file))












