import os
import sys
import getopt

from tools.utils import get_cmd_args


def txt_to_list(input_file_destination):
    handler = open(input_file_destination)
    txt_list = handler.readlines()
    return txt_list

def remove_newlinetag(some_list):
    some_list_newlineremoved = []
    for entry in some_list:
        some_list_newlineremoved.append(entry.rstrip())

    return some_list_newlineremoved

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

def nt_sequence_list_to_fasta(nt_sequence_list, output_directory, output_file_name):
    handler = open(output_directory + "/" + output_file_name + ".fasta", "w")
    handler.write(">" + output_file_name)
    handler.write("\n")

    for entry in nt_sequence_list:
        handler.write(entry)
        handler.write("\n")
    handler.close()

def barcodes_txt_to_FASTA(input_file_destination, output_directory, output_file_name):
    cleaned_list = remove_newlinetag(txt_to_list(input_file_destination))
    type_to_be_removed = type_remove(cleaned_list)
    if type_to_be_removed == "5Biosg":
        cleaned_list_2 = remove_5Biosg(cleaned_list)
    elif type_to_be_removed == "5Phos":
        cleaned_list_2 = remove_5Phos(cleaned_list)
    nt_sequence_list_to_fasta(cleaned_list_2, output_directory, output_file_name)

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
