def txt_to_list(path_to_txt):
    handler = open(path_to_txt)
    return handler.readlines()

def remove_newlinetag(some_list):
    some_list_newlineremoved = []
    for entry in some_list:
        some_list_newlineremoved.append(entry.rstrip())

    return some_list_newlineremoved

def remove_fasta_header(some_list):
    return some_list[1:]

def extract_barcodes(some_list, UMI=False):
    extracted_barcodes = []
    if UMI:
        for barcode in some_list:
            extracted_barcodes.append(barcode[32:40])
    else:
        for barcode in some_list:
            extracted_barcodes.append(barcode[15:23])
    return extracted_barcodes


def make_barcode_combinations(bc1_path, bc2_path, bc3_path):
    bc1_cleaned = remove_fasta_header(remove_newlinetag(txt_to_list(bc1_path)))
    bc1_extracted = extract_barcodes(bc1_cleaned)

    bc2_cleaned = remove_fasta_header(remove_newlinetag(txt_to_list(bc2_path)))
    bc2_extracted = extract_barcodes(bc2_cleaned)

    bc3_cleaned = remove_fasta_header(remove_newlinetag(txt_to_list(bc3_path)))
    bc3_extracted = extract_barcodes(bc3_cleaned, True)

    combined_bcs = []

    for bc1 in bc1_extracted:
        for bc2 in bc2_extracted:
            for bc3 in bc3_extracted:
                combined_bcs.append(bc1 + bc2 + bc3)

    return combined_bcs


def nt_sequence_list_to_file(nt_sequence_list, output_directory, output_file_name, type):
    handler = open(output_directory + "/" + output_file_name + "." + type, "w")
    comb_num = 1

    if type == "fasta":
        for entry in nt_sequence_list:
            handler.write(">comb_" + str(comb_num))
            handler.write("\n")
            handler.write(entry)
            handler.write("\n")
            comb_num += 1
    elif type == "txt":
        for entry in nt_sequence_list:
            handler.write(entry)
            handler.write("\n")
            comb_num += 1
    handler.close()


bc1_path = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper/r1barcodes.fasta"
bc2_path = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper/r2barcodes.fasta"
bc3_path = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper/r3barcodes.fasta"
output_directory = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcode_reference"

barcode_combinations = make_barcode_combinations(bc1_path, bc2_path, bc3_path)
nt_sequence_list_to_file(barcode_combinations, output_directory, "barcode_combinations", "txt")
