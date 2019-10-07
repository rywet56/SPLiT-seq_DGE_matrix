from scripts.file_input_output import *


input_file = "/Users/manuel/Desktop/test.fastq"

reference_list = read_from_file(input_file = input_file, file_type = "fastq", fastq_reads = True)

print(reference_list)