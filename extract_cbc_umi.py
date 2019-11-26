from tools.file_input_output import read_from_file, write_to_fastq
from tools.utils import get_cmd_args, get_resources_used


def get_bcs_umis_queryname(path_to_bc_reads):
    """
    reads in the bc_read.fastq file, extracts the 3 BC's and the UMI, lastly combined the
    3 BC's to one overal cellular BC
    :return: [(query_name, barcode_seq, qual_score, umi_seq, umi_score),(),...]
    """
    bc_reads_list = read_from_file(input_file=path_to_bc_reads, file_type="fastq_all")
    bc_list = [None]*len(bc_reads_list)
    umi_list = [None]*len(bc_reads_list)

    i = 0
    for read in bc_reads_list:
        query_name = read[0]
        bc = read[1][10:18] + read[1][48:56] + read[1][86:94]
        bc_qual = read[2][10:18] + read[2][48:56] + read[2][86:94]
        umi = read[1][0:10]
        umi_qual = read[2][0:10]
        bc_list[i] = [query_name, bc, bc_qual]
        umi_list[i] = [query_name, umi, umi_qual]
        i += 1

    return bc_list, umi_list


@get_resources_used
def extract_bc_umi_to_fastq(path_to_reads, out_dir,  bc_out_filename, umi_out_filename):
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


# extract_bc_umi_to_fastq("/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/SRR6750059_2",
#                         "/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs",
#                         "extracted_bcs",
#                         "extracted_umis")

def main(cmd_args):
    path_to_reads = cmd_args["bc_reads"]
    out_dir = cmd_args["out_dir"]
    bc_out_filename = cmd_args["cbc_out_name"]
    umi_out_filename = cmd_args["umi_out_name"]

    extract_bc_umi_to_fastq(path_to_reads=path_to_reads,
                            out_dir=out_dir,
                            bc_out_filename=bc_out_filename,
                            umi_out_filename=umi_out_filename)


if __name__ == "__main__":
    main(get_cmd_args())