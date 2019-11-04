import pysam

from tools.file_input_output import read_from_file

# sam_in_path = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/aligned_genomic_reads/test.sam"
# sam_in = pysam.AlignmentFile(sam_in_path, "r")


# sam_list = read_from_file(input_file=sam_in_path, file_type="sam")

# sam = pysam.AlignmentFile(sam_in_path, "r")
# input_list = []
# for query in sam.fetch():
#     query_no = int(query.query_name.split(".")[1])
#     input_list.append([query, query_no])

def bubble_sort(some_list):
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(len(some_list)-1):
            if some_list[i + 1][1] < some_list[i][1]:
                old = some_list[i]
                some_list[i] = some_list[i + 1]
                some_list[i + 1] = old
                unsorted = True
    return some_list

def sort_sam(sam):
    input_list = []
    for query in sam.fetch():
        query_no = int(query.query_name.split(".")[1])
        input_list.append([query, query_no])
    return bubble_sort(input_list)
