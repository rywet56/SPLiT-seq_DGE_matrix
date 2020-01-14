from tools.file_input_output import write_to_txt, read_from_file
from tools.utils import get_cmd_args


def extract_barcodes(some_list, UMI=False):
    extracted_barcodes = []
    if UMI:
        for barcode in some_list:
            extracted_barcodes.append(barcode[32:40])
            print(barcode)
    else:
        for barcode in some_list:
            extracted_barcodes.append(barcode[15:23])
            print(barcode)
    return extracted_barcodes


def make_barcode_combinations(bc1_path, bc2_path, bc3_path):
    # bc1_cleaned = remove_fasta_header(remove_newlinetag(txt_to_list(bc1_path)))
    bc1_cleaned = read_from_file(input_file=bc1_path, file_type="txt")
    bc1_extracted = extract_barcodes(bc1_cleaned)

    bc2_cleaned = read_from_file(input_file=bc2_path, file_type="txt")
    bc2_extracted = extract_barcodes(bc2_cleaned)

    bc3_cleaned = read_from_file(input_file=bc3_path, file_type="txt")
    bc3_extracted = extract_barcodes(bc3_cleaned, True)

    combined_bcs = []

    for bc1 in bc1_extracted:
        for bc2 in bc2_extracted:
            for bc3 in bc3_extracted:
                combined_bcs.append(bc1 + bc2 + bc3)

    return combined_bcs

# delete after systemwide test
# def nt_sequence_list_to_file(nt_sequence_list, output_directory, output_file_name, type):
#     handler = open(output_directory + "/" + output_file_name + "." + type, "w")
#     comb_num = 1
#
#     if type == "fasta":
#         for entry in nt_sequence_list:
#             handler.write(">comb_" + str(comb_num))
#             handler.write("\n")
#             handler.write(entry)
#             handler.write("\n")
#             comb_num += 1
#     elif type == "txt":
#         for entry in nt_sequence_list:
#             handler.write(entry)
#             handler.write("\n")
#             comb_num += 1
#     handler.close()


# bc1_path = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper/r1barcodes.fasta"
# bc2_path = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper/r2barcodes.fasta"
# bc3_path = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper/r3barcodes.fasta"
# output_directory = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcode_reference"
# nt_sequence_list_to_file(barcode_combinations, output_directory, "barcode_combinations", "txt")
def bc_combinations_to_fasta(barcode_combinations, out_put_dir, out_filename):
    handler = open(out_put_dir + "/" + out_filename + ".fasta", 'w')
    chromosome = 0
    for comb in barcode_combinations:
        handler.write(">" + str(chromosome))
        handler.write("\n")
        handler.write(str(comb))
        handler.write("\n")
        chromosome += 1


def main(cmd_args):
    bc1_path = cmd_args["bc1"]
    bc2_path = cmd_args["bc2"]
    bc3_path = cmd_args["bc3"]
    out_put_dir = cmd_args["out_dir"]

    barcode_combinations = make_barcode_combinations(bc1_path, bc2_path, bc3_path)
    write_to_txt(barcode_combinations, out_put_dir, "barcode_combinations")
    bc_combinations_to_fasta(barcode_combinations, out_put_dir, "barcode_combinations")


if __name__ == "__main__":
    main(get_cmd_args())