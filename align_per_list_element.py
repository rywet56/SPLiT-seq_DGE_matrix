import sys
from tools.file_input_output import *
from tools.utils import calculate_runtime, return_cmd_args
"""
####### core algorithm of alignment problem
"""


def align_per_list_element(bc_list, query):
    edit_distance_dic = {}
    bc_comb_no = 0
    for bc_comb in bc_list:
        edit_distance = 0
        for base_no in range(len(query) - 1):
            if query[base_no] != bc_comb[base_no]:
                edit_distance += 1
        edit_distance_dic[bc_comb_no] = edit_distance
        bc_comb_no += 1
        if edit_distance == 0:
            print("hey")

    return edit_distance_dic[min(edit_distance_dic)]


def align_per_list_element_2(bc_list, query):
    edit_distance_dic = {}
    bc_comb_no = 0
    for bc_comb in bc_list:
        edit_distance = sum(c1 != c2 for c1, c2 in zip(query, bc_comb))
        edit_distance_dic[bc_comb_no] = edit_distance
        bc_comb_no += 1
    return edit_distance_dic[min(edit_distance_dic)]


def align_string_per_list_element_3(bc_list, query):
    edit_distance_dic = {}
    bc_comb_no = 0
    no_of_barcode_combs = len(bc_list)

    while bc_comb_no < no_of_barcode_combs:
        edit_distance = 0
        for base_no in range(len(query) - 1):
            if query[base_no] != bc_list[bc_comb_no][base_no]:
                edit_distance += 1
            if edit_distance >= 6:
                if base_no < 8:
                    bc_comb_no += 9215  # +1 is added after breaking out
                    break
                elif base_no < 16:
                    bc_comb_no += 95  # +1 is added after breaking out
                    break
                break

        edit_distance_dic[bc_comb_no] = edit_distance
        if edit_distance == 0:
            break  # only valid if edit distance among all BC combinations is big enough
        bc_comb_no += 1

    # best_postition = min(edit_distance_dic, key=edit_distance_dic.get)
    # return [best_postition, edit_distance_dic[best_postition]]
    return get_read_summary(edit_distance_dic, query)


"""
####### alignment applied to all barcode_reads
"""


@calculate_runtime
def align_list_entries(reference_list, query_list, output_directory, output_file_name):
    query_align_pos_list = []
    for query in query_list:
        query_align_pos_list.append(align_string_per_list_element_3(reference_list, query))

    write_read_summary_to_txt_enduser(query_align_pos_list, output_directory, output_file_name)
    write_read_summary_statistics_to_txt_2(query_align_pos_list, output_directory, output_file_name)
    return query_align_pos_list


"""
####### calculate and output alignment summaries
"""


def get_read_summary(edit_distance_dic, query):
    """
    :param edit_distance_dic: {ref_seq_line_number:ED_to_this_ref_seq} e.g. {2345:2, 123:0, ...,}
    :param query: read seq. that has been aligned to ref_seq in above dictionary
    :return: list containing information about alignment of query to all relevant reference sequences
    The first entry in each sub list returns the amount of barcodes the read mapped to with ED of n (0, 1, ..., ).
    The second entry in each sub list returns the barcode numbers that the read mapped to with ED of n (0, 1, ..., ).
    [query_seq, [# alignments with ED 0, line numbers of all aligned ref. seq with ED1], [..., ...], [] ,... ]
    e.g. ['ACGTGTCATG', [3, [2314, 175, 1893]], [1, [345, 1948, 1493]], [], ...,]
    """
    read_summary = []

    ED0_dic = dict(filter(lambda entry: entry[1] == 0, edit_distance_dic.items()))
    ED1_dic = dict(filter(lambda entry: entry[1] == 1, edit_distance_dic.items()))
    ED2_dic = dict(filter(lambda entry: entry[1] == 2, edit_distance_dic.items()))
    ED3_dic = dict(filter(lambda entry: entry[1] == 3, edit_distance_dic.items()))
    ED4_dic = dict(filter(lambda entry: entry[1] == 4, edit_distance_dic.items()))
    ED5_dic = dict(filter(lambda entry: entry[1] == 5, edit_distance_dic.items()))

    return [query, [len(ED0_dic), list(ED0_dic.keys())], [len(ED1_dic), list(ED1_dic.keys())],
            [len(ED2_dic), list(ED2_dic.keys())], [len(ED3_dic), list(ED3_dic.keys())],
            [len(ED4_dic), list(ED4_dic.keys())], [len(ED5_dic), list(ED5_dic.keys())]]


def write_read_summary_to_txt_enduser(summary_list, output_directory, output_file_name):
    handler = open(output_directory + "/" + output_file_name + ".txt", "w")

    for i in range(len(summary_list)):
        handler.write(str(summary_list[i][0]))  # query seqeunce
        handler.write("\n")
        handler.write("ED = 0: ")
        handler.write(str(summary_list[i][1][0]))  # amount of reads with ED = 0
        handler.write(str(summary_list[i][1][1]))  # positions to which ED = 0
        handler.write("\n")
        handler.write("ED = 1: ")
        handler.write(str(summary_list[i][2][0]))  # amount of reads with ED = 1
        handler.write(str(summary_list[i][2][1]))  # positions to which ED = 1
        handler.write("\n")
        handler.write("ED = 2: ")
        handler.write(str(summary_list[i][3][0]))  # amount of reads with ED = 2
        handler.write(str(summary_list[i][3][1]))  # positions to which ED = 2
        handler.write("\n")
        handler.write("ED = 3: ")
        handler.write(str(summary_list[i][4][0]))  # amount of reads with ED = 2
        handler.write(str(summary_list[i][4][1]))  # positions to which ED = 2
        handler.write("\n")
        handler.write("ED = 4: ")
        handler.write(str(summary_list[i][5][0]))  # amount of reads with ED = 2
        handler.write(str(summary_list[i][5][1]))  # positions to which ED = 2
        handler.write("\n")
        handler.write("ED = 5: ")
        handler.write(str(summary_list[i][6][0]))  # amount of reads with ED = 2
        handler.write(str(summary_list[i][6][1]))  # positions to which ED = 2
        handler.write("\n")
        handler.write("-------------------------------------")
        handler.write("\n")
    handler.close()


def write_read_summary_to_txt_internal(summary_list, output_directory, output_file_name):
    handler = open(output_directory + "/" + output_file_name + ".txt", "w")

    for i in range(len(summary_list)):  # go through summaries of all aligned reads
        handler.write(str(summary_list[i][0]))  # query sequence
        handler.write("\n")

        for ED in range(1, len(summary_list[i])):
            # print("edit distance: " + str(edit_distance))
            handler.write(str(summary_list[i][ED][0]))  # amount of reads with ED = n
            handler.write("\t")

            for position in summary_list[i][ED][1]:  # positions to which ED = 0
                handler.write(str(position))
                handler.write("\t")

            handler.write("\n")

    handler.close()


def write_read_summary_statistics_to_txt(summary_list, output_directory, output_file_name):
    handler = open(output_directory + "/" + output_file_name + "_statistics" + ".txt", "w")

    ED0 = 0
    ED1 = 0
    ED2 = 0
    ED3 = 0
    ED4 = 0
    ED5 = 0

    for entry in summary_list:
        ED0 += entry[1][0]
        ED1 += entry[2][0]
        ED2 += entry[3][0]
        ED3 += entry[4][0]
        ED4 += entry[5][0]
        ED5 += entry[6][0]

    handler.write("ED0" + "\t" + str(ED0) + "\n")
    handler.write("ED1" + "\t" + str(ED1) + "\n")
    handler.write("ED2" + "\t" + str(ED2) + "\n")
    handler.write("ED3" + "\t" + str(ED3) + "\n")
    handler.write("ED4" + "\t" + str(ED4) + "\n")
    handler.write("ED5" + "\t" + str(ED5) + "\n")

    handler.close()


def write_read_summary_statistics_to_txt_2(summary_list, output_directory, output_file_name):
    handler = open(output_directory + "/" + output_file_name + "_statistics" + ".txt", "w")

    ED_grand = 0
    ED_total = [0] * 6
    ED_first = [0] * 6  # every entry corresponds to number of first alignment(s) with ED = 0, 1, ... , 5
    match_1 = [0] * 6
    match_2 = [0] * 6
    match_3 = [0] * 6


    # count number of first alginments for every ED 0 through 5
    for entry in summary_list:

        for i in range(1, 6):
            ED_grand += entry[i][0]
            ED_total[i-1] += entry[i][0]

        if entry[1][0] > 0:  # ED = 0   --> first alignment appears with ED = 0
            ED_first[0] += 1
            if entry[1][0] == 1:
                match_1[0] += 1
            elif entry[1][0] == 2:
                match_2[0] += 1
            elif entry[1][0] == 3:
                match_3[0] += 1

        elif entry[2][0] > 0:   # ED = 1    --> first alignment appears with ED = 1
            ED_first[1] += 1
            if entry[2][0] == 1:
                match_1[1] += 1
            elif entry[2][0] == 2:
                match_2[1] += 1
            elif entry[2][0] == 3:
                match_3[1] += 1

        elif entry[3][0] > 0:  # ED = 2     --> first alignment appears with ED = 2
            ED_first[2] += 1
            if entry[3][0] == 1:    # 1 aligned position with ED=2
                match_1[2] += 1
            elif entry[3][0] == 2:  # 2 aligned positions with ED=2
                match_2[2] += 1
            elif entry[3][0] == 3:  # 3 aligned positions with ED=2
                match_3[2] += 1

        elif entry[4][0] > 0:  # ED = 3     --> first alignment appears with ED = 3
            ED_first[3] += 1
            if entry[3][0] == 1:    # 1 aligned position with ED=3
                match_1[3] += 1
            elif entry[3][0] == 2:  # 2 aligned positions with ED=3
                match_2[3] += 1
            elif entry[3][0] == 3:  # 3 aligned positions with ED=3
                match_3[3] += 1

    handler.write("ED" + "\t" + "all" +"\t" + "1stA" + "\t" + "A:1" + "\t" + "A:2" + "\t" + "A:3" + "\n")

    # write summary statistic to file
    for ED in range(len(ED_first)):
        handler.write(str(ED) + "\t")
        handler.write(str(ED_total[ED]) + "\t")
        handler.write(str(ED_first[ED]) + "\t")
        handler.write(str(match_1[ED]) + "\t")
        handler.write(str(match_2[ED]) + "\t")
        handler.write(str(match_3[ED]) + "\t")
        handler.write("\n")

    # write some explanations
    handler.write("\n")
    handler.write("The total number of alignment events was: " + str(ED_grand) + "\n")
    handler.write("all --> amount of alignments that were made with ED = n {0, ..., 5)" + "\n")
    handler.write("1stA --> amount of reads whose first alignment was possible with ED = n {0, ..., 5)" + "\n")
    handler.write("A:1 --> amount of reads that aligned exactly ones to any of the barcode_combination with ED = n {0, ..., 5)" + "\n")
    handler.write("A:2 --> amount of reads that aligned exactly twice to any of the barcode_combination with ED = n {0, ..., 5)" + "\n")
    handler.write("A:3 --> amount of reads that aligned exactly three times to any of the barcode_combination with ED = n {0, ..., 5)" + "\n")
    handler.close()


def main(cmd_args):
    path_to_reference, path_to_extracted_barcodes_txt, out_put_dir = return_cmd_args(cmd_args)
    reference_list = read_from_file(input_file = path_to_reference, file_type = "fasta")
    extracted_barcodes_list = read_from_file(input_file = path_to_extracted_barcodes_txt, file_type = "txt")
    align_list_entries(reference_list, extracted_barcodes_list, out_put_dir, "alignment_summary")


if __name__ == "__main__":
    main(sys.argv[1:])


########################################
####### TESTS ##########################
########################################


# home_dir = '/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/barcode_correction/barcode_correction_pseudo_alignment'
# path_to_reference = home_dir + '/reference/barcode_combinations.fasta'
# # # path_to_fastq = '/Users/manuel/Downloads/test_1000000.fastq'
# out_put_dir = home_dir + '/results'
# # # extract_barcodes_to_txt(path_to_fastq, out_put_dir, "extracted_barcodes")
# path_to_extracted_barcodes_txt = home_dir + '/barcode_reads/extracted_barcodes_500.txt'
# #
# reference_list = fasta_to_list(path_to_reference)
# extracted_barcodes_list = txt_to_list(path_to_extracted_barcodes_txt)
# #
#
# # print(sys.executable)
#
# align_list_entries(reference_list, extracted_barcodes_list, out_put_dir, "alignment_summary")
#
# # main([path_to_reference, path_to_extracted_barcodes_txt, out_put_dir])
