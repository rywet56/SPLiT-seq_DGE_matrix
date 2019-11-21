from tools.file_input_output import read_from_file, write_to_fastq, write_to_txt


def get_aligned_reads(path_to_sam_file, barcode_comb_list):
    sam_list = read_from_file(file_type="sam", input_file=path_to_sam_file)
    aligned_reads = []
    qual = []
    for sam in sam_list:
        if sam[0].has_tag("AS") and sam[0].get_tag('NM') < 1:
            correct_seq_pos = sam[0].tid
            aligned_reads.append(barcode_comb_list[correct_seq_pos])
            qual.append(sam[0].mapping_quality)
    # ED = 0
    # for sam in sam_list:
    #     if sam[0].has_tag("AS"):
    #         aligned_reads.append(sam[0])
    #     if sam[0].has_tag('NM') and sam[0].get_tag('NM') > 0:
    #         ED += 1
    return aligned_reads


def get_barcode_combinations_list(path_to_bc_comb):
    '''
    reads in a .fasta file and saves the read in this file.
    '''
    handler = open(path_to_bc_comb, "r")
    bc_comb = handler.readlines()
    bc_comb_list = [None]*int((len(bc_comb)/2))

    i = 0
    k = 1
    while i < len(bc_comb_list):
        bc_comb_list[i] = bc_comb[k]
        i += 1
        k += 2

    return bc_comb_list


def sam_to_fastq(sam_list, out_dir, out_filename):
    fastq_list = [""]*len(sam_list)
    i = 0
    for sam in sam_list:
        fastq_list[i] = [sam.query_name, sam.query_sequence, sam.query_qualities]
        i += 1

    write_to_fastq(fastq_list=fastq_list, output_directory=out_dir, output_file_name=out_filename, mode="write")


def list_to_txt(read_list, out_dir, out_filename):
    txt_list = [""]*len(read_list)
    i = 0
    for entry in read_list:
        txt_list[i] = entry
        i += 1

    write_to_txt(input_list=txt_list, output_directory=out_dir, output_file_name=out_filename)


def aligned_reads_to_fastq(path_to_sam_file, out_dir, out_filename):
    aligned_reads = get_aligned_reads(path_to_sam_file)
    sam_to_fastq(aligned_reads, out_dir, out_filename)


def aligned_reads_to_txt(path_to_sam_file, path_to_bc_comb, out_dir, out_filename):
    barcode_comb_list = get_barcode_combinations_list(path_to_bc_comb)
    aligned_reads = get_aligned_reads(path_to_sam_file, barcode_comb_list)
    list_to_txt(aligned_reads, out_dir, out_filename)


# aligned_reads_to_fastq(path_to_sam_file="/Users/manuel/Desktop/bowtie_strategy/aligned_bcs.sam",
#                        out_dir="/Users/manuel/Desktop/bowtie_strategy",
#                        out_filename="selected_barcodes")

#
aligned_reads_to_txt(path_to_sam_file="/Users/manuel/Desktop/bowtie_strategy/aligned_bcs.sam",
                    path_to_bc_comb="/Users/manuel/Desktop/bowtie_strategy/barcode_combinations.fasta",
                       out_dir="/Users/manuel/Desktop/bowtie_strategy",
                       out_filename="selected_barcodes")

# l = get_barcode_combinations_list("/Users/manuel/Desktop/bowtie_strategy/barcode_combinations.fasta")
# print(str(l[0]))