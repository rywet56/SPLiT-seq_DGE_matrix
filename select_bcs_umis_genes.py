from filter_barcodes_advanced import get_number_of_low_quality_bases
from tools.file_input_output import read_from_file, write_to_fastq, write_to_txt
from tools.utils import get_resources_used, get_cmd_args
from memory_profiler import profile


def get_aligned_selected_reads(path_to_sam_file, barcode_comb_list):
    '''
    Reads in contents of .bam file and copies those reads to sam_list that could be aligned
    and have an ED < 1 to the aligned barcode_combinaiton. Then (this only makes sense if ED > 0)
    reads are corrected with the respective barcode from barcode_comb_list.
    :param path_to_sam_file:
    :param barcode_comb_list:
    :return: a list that contains 0 for reads that did not pass the selection criteria and a read
    sequence for those read that did pass the selection criteria.
    '''
    sam_list = read_from_file(file_type="sam", input_file=path_to_sam_file)
    aligned_reads = [0]*len(sam_list)

    i = 0
    for sam in sam_list:
        if sam[0].has_tag("AS") and sam[0].get_tag('NM') < 1:
            correct_seq_pos = sam[0].tid
            aligned_reads[i] = barcode_comb_list[correct_seq_pos]
        else:
            aligned_reads[i] = 0
        i += 1

    return aligned_reads


def get_barcode_combinations_list(path_to_bc_comb):
    '''
    reads in a .fasta file and saves the read in this file.
    '''
    handler = open(path_to_bc_comb, "r")
    bc_comb = handler.readlines()
    bc_comb_list = [None] * int((len(bc_comb) / 2))

    i = 0
    k = 1
    while i < len(bc_comb_list):
        bc_comb_list[i] = bc_comb[k].split('\n')[0]
        i += 1
        k += 2

    return bc_comb_list


def sam_to_fastq(sam_list, out_dir, out_filename):
    fastq_list = [""] * len(sam_list)
    i = 0
    for sam in sam_list:
        fastq_list[i] = [sam.query_name, sam.query_sequence, sam.query_qualities]
        i += 1

    write_to_fastq(fastq_list=fastq_list, output_directory=out_dir, output_file_name=out_filename, mode="write")


def sel_items_to_file(read_list, out_dir, out_filename, file_type):
    out_list = []

    if file_type == "txt":
        for entry in read_list:
            if entry != 0:
                out_list.append(entry)
        write_to_txt(input_list=out_list, output_directory=out_dir, output_file_name=out_filename)
    elif file_type == "fastq":
        for entry in read_list:
            if entry != 0:
                # name = entry[0].split(" ")[0]  # a non-elegant way to fix some mess up
                # out_list.append([name, entry[1], entry[2]])
                out_list.append(entry)
        write_to_fastq(fastq_list=out_list, output_directory=out_dir, output_file_name=out_filename)


def select_bcs_umis_gens(path_to_umis_fastq, path_to_gen_fastq, aligned_sel_bcs):
    # read in umis and genes
    umis_list = read_from_file(input_file=path_to_umis_fastq, file_type="fastq_all")
    gens_list = read_from_file(input_file=path_to_gen_fastq, file_type="fastq_all")
    # list that will be populated with sel umis (0s or sequences)
    sel_umis = [0]*len(aligned_sel_bcs)

    for pos in range(len(umis_list)):
        number_low_quality_bases = get_number_of_low_quality_bases(umis_list[pos][2])
        if number_low_quality_bases > 1 or aligned_sel_bcs[pos] == 0:
            aligned_sel_bcs[pos] = 0
            gens_list[pos] = 0
        else:
            sel_umis[pos] = umis_list[pos][1]

    return aligned_sel_bcs, sel_umis, gens_list

# def aligned_reads_to_fastq(path_to_sam_file, out_dir, out_filename):
#     aligned_reads = get_aligned_reads(path_to_sam_file)
#     sam_to_fastq(aligned_reads, out_dir, out_filename)
@get_resources_used
# @profile
def aligned_reads_to_txt(path_to_cbcs_sam, path_to_bc_comb, path_to_umis_fastq, path_to_gen_fastq, out_dir, out_filename_bcs,
                         out_filename_umis, out_filename_gen):
    # get list that maps bc_combs to "chrosomsome numbers"
    barcode_comb_list = get_barcode_combinations_list(path_to_bc_comb)
    # get bcs that did align with ED = 0
    sel_bcs = get_aligned_selected_reads(path_to_cbcs_sam, barcode_comb_list)
    # continue selection of bcs based on UMI quality
    sel_bcs, sel_umis, sel_gens = select_bcs_umis_gens(path_to_umis_fastq, path_to_gen_fastq, sel_bcs)
    # write gens, bcs, umis to file
    sel_items_to_file(sel_umis, out_dir, out_filename_umis, file_type="txt")
    sel_items_to_file(sel_bcs, out_dir, out_filename_bcs, file_type="txt")
    sel_items_to_file(sel_gens, out_dir, out_filename_gen, file_type="fastq")



# aligned_reads_to_txt(path_to_cbcs_sam="/Users/manuel/Desktop/bowtie_strategy/aligned_bcs.sam",
#                      path_to_bc_comb="/Users/manuel/Desktop/bowtie_strategy/barcode_combinations.fasta",
#                      path_to_umis_fastq="/Users/manuel/Desktop/bowtie_strategy/extracted_umis.fastq",
#                      path_to_gen_fastq="/Users/manuel/Desktop/bowtie_strategy/SRR6750059_1_1mio.fastq",
#                      out_dir="/Users/manuel/Desktop/bowtie_strategy",
#                      out_filename_bcs="selected_barcodes",
#                      out_filename_umis="selected_umis",
#                      out_filename_gen="selected_gens")


def main(cmd_args):
    path_to_cbcs_sam = cmd_args["sam_in"]
    path_to_bc_comb = cmd_args["cbc_comb"]
    path_to_umis_fastq = cmd_args["umi_in"]
    path_to_gen_fastq = cmd_args["gen_reads"]
    out_dir = cmd_args["out_dir"]
    out_filename_bcs = cmd_args["cbc_out_name"]
    out_filename_umis = cmd_args["umi_out_name"]
    out_filename_gen = cmd_args["gene_out_name"]

    aligned_reads_to_txt(path_to_cbcs_sam=path_to_cbcs_sam,
                         path_to_bc_comb=path_to_bc_comb,
                         path_to_umis_fastq=path_to_umis_fastq,
                         path_to_gen_fastq=path_to_gen_fastq,
                         out_dir=out_dir,
                         out_filename_bcs=out_filename_bcs,
                         out_filename_umis=out_filename_umis,
                         out_filename_gen=out_filename_gen)

    # aligned_reads_to_txt(path_to_cbcs_sam="/Users/manuel/Desktop/bowtie_strategy/aligned_bcs.sam",
    #                      path_to_bc_comb="/Users/manuel/Desktop/bowtie_strategy/barcode_combinations.fasta",
    #                      path_to_umis_fastq="/Users/manuel/Desktop/bowtie_strategy/extracted_umis.fastq",
    #                      path_to_gen_fastq="/Users/manuel/Desktop/bowtie_strategy/SRR6750059_1_1mio.fastq",
    #                      out_dir="/Users/manuel/Desktop/bowtie_strategy",
    #                      out_filename_bcs="selected_barcodes",
    #                      out_filename_umis="selected_umis",
    #                      out_filename_gen="selected_gens")


if __name__ == "__main__":
    main(get_cmd_args())
