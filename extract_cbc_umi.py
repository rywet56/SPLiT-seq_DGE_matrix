from tools.file_input_output import read_from_file, write_to_fastq
from tools.utils import get_cmd_args, get_resources_used, QSanger_to_Phred33
from memory_profiler import profile
from Bio import SeqIO


### THIS FUNCTION IS NOT USED ANYMORE
def get_bcs_umis_queryname(path_to_bc_reads, mode="SPLiT"):
    """
    reads in the bc_read.fastq file, extracts the 3 BC's and the UMI, lastly combined the
    3 BC's to one overal cellular BC
    :return: [(query_name, barcode_seq, qual_score, umi_seq, umi_score),(),...]
    """
    bc_reads_list = read_from_file(input_file=path_to_bc_reads, file_type="fastq_all")
    bc_list = [None] * len(bc_reads_list)
    umi_list = [None] * len(bc_reads_list)

    if mode == "SPLiT":
        i = 0
        for i, read in enumerate(bc_reads_list):
            query_name = read[0]
            bc = read[1][10:18] + read[1][48:56] + read[1][86:94]
            bc_qual = read[2][10:18] + read[2][48:56] + read[2][86:94]
            umi = read[1][0:10]
            umi_qual = read[2][0:10]
            bc_list[i] = [query_name, bc, bc_qual]
            umi_list[i] = [query_name, umi, umi_qual]
            # i += 1
    if mode == "10X":
        for i, read in enumerate(bc_reads_list):
            query_name = read[0]
            bc = read[1][0:16]
            bc_qual = read[2][0:16]
            umi = read[1][16:]
            umi_qual = read[2][16:]
            bc_list[i] = [query_name, bc, bc_qual]
            umi_list[i] = [query_name, umi, umi_qual]

    return bc_list, umi_list


### THIS FUNCTION IS NOT USED ANYMORE
# @get_resources_used
# @profile
def extract_bc_umi_to_fastq(path_to_reads, out_dir, bc_out_filename, umi_out_filename):
    '''
    Extracts the barcodes and umis from bc_read.fastq file. Then saves them in two separate .fastq files
    :param path_to_reads:
    :param out_dir:
    :param bc_out_filename:
    :param umi_out_filename:
    :return:
    '''

    bcs, umis = get_bcs_umis_queryname(path_to_bc_reads=path_to_reads)

    write_to_fastq(fastq_list=bcs, output_directory=out_dir, output_file_name=bc_out_filename, mode="write")
    write_to_fastq(fastq_list=umis, output_directory=out_dir, output_file_name=umi_out_filename, mode="write")


# @get_resources_used
# @profile
def extract_cbc_umi_to_fastq_directly(path_to_reads, out_dir, bc_out_filename, umi_out_filename, mode):
    write_bcs = open(out_dir + "/" + bc_out_filename + ".fastq", "w")
    write_umis = open(out_dir + "/" + umi_out_filename + ".fastq", "w")

    if mode == "SPLiT":
        for record in SeqIO.parse(path_to_reads, "fastq"):
            # get read quality - only has to be done once
            read_qual = ''.join(QSanger_to_Phred33(record.letter_annotations["phred_quality"]))

            # extracs CBC and write to file
            write_bcs.write("@" + str(record.description) + "\n")
            write_bcs.write(str(record.seq[10:18] + record.seq[48:56] + record.seq[86:94]) + "\n")
            write_bcs.write("+\n")
            write_bcs.write(str(read_qual[10:18] + read_qual[48:56] + read_qual[86:94]) + "\n")

            # extract UMI and write to file
            write_umis.write("@" + str(record.description) + "\n")
            write_umis.write(str(record.seq[0:10]) + "\n")
            write_umis.write("+\n")
            write_umis.write(str(read_qual[0:10]) + "\n")

    elif mode == "10X":
        for record in SeqIO.parse(path_to_reads, "fastq"):
            # get read quality - only has to be done once
            read_qual = ''.join(QSanger_to_Phred33(record.letter_annotations["phred_quality"]))

            # extracs CBC and write to file
            write_bcs.write("@" + str(record.description) + "\n")
            write_bcs.write(str(record.seq[0:16]) + "\n")
            write_bcs.write("+\n")
            write_bcs.write(str(read_qual[0:16]) + "\n")

            # extract UMI and write to file
            write_umis.write("@" + str(record.description) + "\n")
            write_umis.write(str(record.seq[16:]) + "\n")
            write_umis.write("+\n")
            write_umis.write(str(read_qual[16:]) + "\n")


def main(cmd_args):
    path_to_reads = cmd_args["bc_reads"]
    out_dir = cmd_args["out_dir"]
    bc_out_filename = cmd_args["cbc_out_name"]
    umi_out_filename = cmd_args["umi_out_name"]
    print("here")
    mode = cmd_args["mode"]


    extract_cbc_umi_to_fastq_directly(path_to_reads=path_to_reads,
                                      out_dir=out_dir,
                                      bc_out_filename=bc_out_filename,
                                      umi_out_filename=umi_out_filename,
                                      mode=mode)


if __name__ == "__main__":
    main(get_cmd_args())
