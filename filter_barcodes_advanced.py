from tools.utils import calculate_runtime, return_cmd_args, get_cmd_args
from tools.file_input_output import *


def align_string_per_list_element_simple(bc_list, query):
    query_tuple = ()
    bc_comb_no = 0
    no_of_barcode_combs = len(bc_list)
    match_found = False

    while bc_comb_no < no_of_barcode_combs:
        edit_distance = 0
        for base_no in range(len(query) - 1):
            if query[base_no] != bc_list[bc_comb_no][base_no]:
                edit_distance += 1
            if edit_distance >= 2:
                if base_no < 8:
                    bc_comb_no += 9215  # +1 is added after breaking out
                    break
                elif base_no < 16:
                    bc_comb_no += 95  # +1 is added after breaking out
                    break
                break

        if edit_distance == 0:
            match_found = True
            break
        elif edit_distance == 1:  # checks again to stop alg from searching if ED was 0
            match_found = True
            break
        bc_comb_no += 1

    if match_found:
        query_tuple = (query, 1)
    else:
        query_tuple = (query, 0)

    return query_tuple


def align_string_per_list_element_comprehensive(bc_list, query):
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

    return get_read_summary(edit_distance_dic, query)  # returns a list containing alignment information
    # return ReadSummary(edit_distance_dic, query)  # returns a GetReadSummary object containing alignment information


@calculate_runtime
def align_list_entries(reference_list, query_list, genomic_reads, out_dir, mode):
    if mode == "simple":
        query_ed_list = []
        for query in query_list:
            query_ed_list.append((align_string_per_list_element_simple(reference_list, query[0]), query[1], query[2], query[3]))
        print("reads have been aligned in mode: simple")
        # structure of quere_ed_list
        # [ ( (bc, True/False), bc_qual, umi, umi_qual ), (), ...]
        filtered_reads_to_files(query_ed_list, genomic_reads, out_dir)
        print("filtered reads have sucessfully been written to files")

    elif mode == "comprehensive":
        query_align_pos_list = []
        for query in query_list:
            query_align_pos_list.append(align_string_per_list_element_comprehensive(reference_list, query[0]))
        print("reads have been aligned in mode: comprehensive")

        write_read_summary_to_txt_enduser(query_align_pos_list, out_dir, "alignment_summary")
        write_read_summary_statistics_to_txt(query_align_pos_list, out_dir, "alignment_summary")
        print("alignment summar and statistics have sucessfully been written to files")
        # function has to be called to write filtered reads to files
        print("filtered reads have sucessfully been written to files")


def filtered_reads_to_files(query_ed_list, genomic_reads, output_directory):

    new_gen_read_list = []
    new_bc_read_list = []
    new_umi_list = []

    for pos in range(len(query_ed_list)):
        num_low_qual_base_umi = get_number_of_low_quality_bases(query_ed_list[pos][3])
        umi_ok = num_low_qual_base_umi < 2

        bc_ok = query_ed_list[pos][0][1]

        if umi_ok and bc_ok:
            new_gen_read_list.append(genomic_reads[pos])
            new_bc_read_list.append(query_ed_list[pos][0][0])
            new_umi_list.append(query_ed_list[pos][2])

    write_to_fastq(new_gen_read_list, output_directory, "filtered_genomic_reads")
    write_to_txt(new_bc_read_list, output_directory, "filtered_bc_reads")
    write_to_txt(new_umi_list, output_directory, "filtered_UMIs")


def get_bcs_umis(path_to_bc_reads):
    """
    reads in the bc_read.fastq file, extracts the 3 BC's and the UMI, lastly combined the
    3 BC's to one overal cellular BC
    :return: [(barcode_seq, qual_score, umi_seq, umi_score),(),...]
    """
    bc_reads_list = read_from_file(input_file=path_to_bc_reads, file_type="fastq_all")
    bc_umi_list = []
    for read in bc_reads_list:
        bc = read[1][10:18] + read[1][48:56] + read[1][86:94]
        bc_qual = read[2][10:18] + read[2][48:56] + read[2][86:94]
        umi = read[1][0:10]
        umi_qual = read[2][0:10]
        bc_umi_list.append((bc, bc_qual, umi, umi_qual))

    return bc_umi_list


def get_number_of_low_quality_bases(qual_score_list, threshold=10):
    number_low_quality_bases = 0
    for score in qual_score_list:
        if score <= threshold:
            number_low_quality_bases += 1

    return number_low_quality_bases


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
    handler = open(output_directory + "/" + output_file_name + "_enduser.txt", "w")

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


def write_read_summary_statistics_to_txt(summary_list, output_directory, output_file_name):
    """
    creates a very detailed and informative overall summary file of alignment statistics
    :param summary_list:
    :param output_directory:
    :param output_file_name:
    :return:
    """
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
    path_to_reference = cmd_args["bc_reference"]
    path_to_barcode_reads = cmd_args["bc_reads"]
    path_to_genomic_reads = cmd_args["gen_reads"]
    out_put_dir = cmd_args["out_dir"]
    mode = cmd_args['mode']

    reference_list = read_from_file(input_file=path_to_reference, file_type="txt")
    barcode_reads_list = get_bcs_umis(path_to_barcode_reads)
    genomic_reads_list = read_from_file(input_file=path_to_genomic_reads, file_type="fastq_all")

    align_list_entries(reference_list, barcode_reads_list, genomic_reads_list, out_dir=out_put_dir, mode=mode)

    # has tobe added as wrapper function
    import os
    import psutil
    process = psutil.Process(os.getpid())
    print("The memory usage was: " + str(process.memory_info().rss/1000000000) + " GB")  # in bytes


if __name__ == "__main__":
    main(get_cmd_args())
