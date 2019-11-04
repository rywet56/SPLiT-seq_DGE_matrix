
def read_file_into_pyhton_list(filepath):
    handler = open(filepath)
    file_content = handler.readlines()
    return file_content

fastq_works = "/Users/manuel/Desktop/test/barcodes_working.fastq"
fastq_does_not_work = "/Users/manuel/Desktop/test/barcodes_notworking.fastq"

print(read_file_into_pyhton_list(fastq_works))
print(read_file_into_pyhton_list(fastq_does_not_work))
