from tools.utils import calculate_runtime, return_cmd_args, get_cmd_args
from tools.file_input_output import *


def align_string_per_list_element(bc_list, query):
    query_ed = ()
    bc_comb_no = 0
    no_of_barcode_combs = len(bc_list)
    match_found = False

    while bc_comb_no < no_of_barcode_combs:
        edit_distance = 0
        for base_no in range(len(query) - 1):
            if query[base_no] != bc_list[bc_comb_no][base_no]:
                edit_distance += 1
            if edit_distance >= 1:
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
        bc_comb_no += 1

    if match_found:
        query_ed = (query, 1)
    else:
        query_ed = (query, 0)

    return query_ed


@calculate_runtime
def align_list_entries(reference_list, query_list, genomic_reads, output_directory, **kwargs):
    query_ed_list = []
    for query in query_list:
        query_ed_list.append(align_string_per_list_element(reference_list, query))

    filtered_reads_to_files(query_ed_list, genomic_reads, output_directory)


def filtered_reads_to_files(query_ed_list, genomic_reads, output_directory):

    new_gen_read_list = []
    new_bc_read_list = []

    for pos in range(len(query_ed_list)):
        if query_ed_list[pos][1]:
            new_gen_read_list.append(genomic_reads[pos])
            new_bc_read_list.append(query_ed_list[pos][0])

    write_to_fastq(new_gen_read_list, output_directory, "filtered_genomic_reads")
    write_to_txt(new_bc_read_list, output_directory, "filtered_bc_reads")


def main(cmd_args):
    # path_to_reference, path_to_extracted_barcodes_txt, path_to_genomic_reads, out_put_dir = return_cmd_args(cmd_args)
    path_to_reference = cmd_args["bc_reference"]
    path_to_extracted_barcodes_txt = cmd_args["bc_reads"]
    path_to_genomic_reads = cmd_args["gen_reads"]
    out_put_dir = cmd_args["out_dir"]

    reference_list = read_from_file(input_file=path_to_reference, file_type="fasta")
    extracted_barcodes_list = read_from_file(input_file=path_to_extracted_barcodes_txt, file_type="txt")
    genomic_reads_list = read_from_file(input_file=path_to_genomic_reads, file_type="fastq_all")
    align_list_entries(reference_list, extracted_barcodes_list, genomic_reads_list, out_put_dir, out_dir=out_put_dir)


if __name__ == "__main__":
    main(get_cmd_args())
