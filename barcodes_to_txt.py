from tools.file_input_output import write_to_txt, read_from_file
from tools.utils import get_cmd_args


def remove_5Phos(some_list):
    Phos_removed = []
    for entry in some_list:
        Phos_removed.append(entry[7:])

    return Phos_removed


def remove_5Biosg(some_list):
    Biosg_removed = []
    for entry in some_list:
        Biosg_removed.append(entry[8:])

    return Biosg_removed


def type_remove(some_list):
    sequence_type_to_be_removed = ''

    if some_list[0][1:7] == "5Biosg":
        sequence_type_to_be_removed = "5Biosg"
    elif some_list[0][1:6] == "5Phos":
        sequence_type_to_be_removed = "5Phos"

    return sequence_type_to_be_removed


def barcodes_txt_to_FASTA(input_file_destination, output_directory, output_file_name):
    barcode_list = read_from_file(file_type = "txt", input_file = input_file_destination)
    type_to_be_removed = type_remove(barcode_list)
    cleaned_barcoed_list = []

    if type_to_be_removed == "5Biosg":
        cleaned_barcoed_list = remove_5Biosg(barcode_list)
    elif type_to_be_removed == "5Phos":
        cleaned_barcoed_list = remove_5Phos(barcode_list)

    write_to_txt(cleaned_barcoed_list, output_directory, output_file_name)


def return_cmd_args(args):

    opts_and_args, args = getopt.getopt(args, "i:o:f:", ["indir=", "outdir=", "outfilename="])

    indir = ''
    outdir = ''
    outfilename = ''

    for opt, arg in opts_and_args:
        if opt in ("-i", "--indir"):
            indir = arg
        elif opt in ("-o", "--outdir"):
            outdir = arg
        elif opt in ("-f", "--outfilename"):
            outfilename = arg

    return indir, outdir, outfilename


def main(cmd_args):
    in_dir = cmd_args["in_dir"]
    out_dir = cmd_args["out_dir"]
    name = cmd_args["file_name"]
    barcodes_txt_to_FASTA(in_dir, out_dir, name)


if __name__ == "__main__":
    main(get_cmd_args())

##########################
# HOW TO USE THIS SCRIPT #
##########################
# This script accepts 3 parameters whose names are self explanatory.
#     --indir <path to the input .txt file>
#     --outdir <path to the output directory>
#     --outfilename <filename of the output .fasta file in the outdir>
#
# The script can be used as follows:
#     home_dir=$(pwd)
#     in1=$home_dir/barcodes/R1_barcodes.txt
#     out1=$home_dir
#     name1="r1barcodes"
#     python3 $home_dir/barcodes_excel_to_FASTA.py \
#         --indir $in1 \
#         --outdir $out1 \
#         --outfilename $name1
#
# Every line in the input file has to have the following structure:
#     /5Phos/CATCGGCGTACGACTAACGTGATATCCACGTGCTTGAG
#         or
#     /5Biosg/CAGACGTGTGCTCTTCCGATCTNNNNNNNNNNAAGGTACAGTGGCCGATGTTTCG
