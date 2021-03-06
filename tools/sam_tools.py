import pysam
from tools.file_input_output import read_from_file, remove_newlinetag


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


def sort_sam_2(sam):
    input_list = []
    for query in sam.fetch():
        query_no = int(query.query_name.split(".")[1])
        input_list.append([query, query_no])
    return bubble_sort(input_list)


# # Check genes added to each read
# sam_in_path = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/sample_data/genfun_tagged_aligned_filtered_reads/genfun_tagged.sam"
# sam_in = pysam.AlignmentFile(sam_in_path, "r")
#
# gene_list = []
# for query in sam_in.fetch():f
#     if query.has_tag('gn'):
#         gene_list.append(query.get_tag('gn'))
#     else:
#         gene_list.append(0)
#
# unique_genes = []
# for gene in gene_list:
#     if gene != 0:
#         if gene not in unique_genes:
#             unique_genes.append(gene)
# print("barcodes and genes in .bam file")
# print("number of genes: " + str(len(unique_genes)))
# print("\n")
#
# # Check number of barcodes and genes used in DGE matrix
# dge_path = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/sample_data/DGE_matrix/sample_dge_matrix.dge"
# handler = open(dge_path)
# dge = handler.readlines()
# dge = remove_newlinetag(dge)
# barcodes = dge[0].split("\t")
# barcodes = barcodes[1:]
#
# genes = []
# for entry in range(1, len(dge)):
#     gene = dge[entry].split("\t")
#     genes.append(gene[0])
#
# print("barcodes and genes in DGE matrix")
# print("number of barcodes: " + str(len(barcodes)))
# print("number of genes: " + str(len(genes)))

def sort_sam_built_in(sam_list):
    '''

    :param sam_list: [ [query, query_no] ... ]
    :return:
    '''
    # construct sam_dic that contains reads from the sam file
    sam_dic = {}
    for entry in sam_list:
        # print(entry[1].split('.'))
        query_no = entry[1].split('.')
        query_no = query_no[0][3:] + query_no[1]
        sam_dic[query_no] = entry[0]

    # sort the sam_dic
    sorted_sam = sorted(sam_dic)

    # convert sorted_sam into a list containing all read-sam objects
    sorted_sam_list = [0]*len(sorted_sam)
    for i in range(len(sorted_sam)):
        sorted_sam_list[i] = sam_dic[sorted_sam[i]]

    return sorted_sam_list

