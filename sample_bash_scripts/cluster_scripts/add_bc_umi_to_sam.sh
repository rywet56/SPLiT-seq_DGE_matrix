#!/usr/bin/env bash

scripts="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix"

path_to_bc="/Users/manuel/Desktop/cbcs_test.txt"
path_to_umi="/Users/manuel/Desktop/umis_test.txt"
sam_in_path="/Users/manuel/Desktop/test.sam"
sam_out_path="/Users/manuel/Desktop"
file_name="out.sam"


python3 $scripts/add_BC_UMI_tags.py \
     --bc_in $path_to_bc \
     --umi_in $path_to_umi \
     --sam_in $sam_in_path \
     --sam_out $sam_out_path \
     --file_name $file_name
