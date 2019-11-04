#!/usr/bin/env bash

scripts="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix"

path_to_bc="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/results/filtered_bc_reads.txt"
path_to_umi="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/results/filtered_UMIs.txt"
sam_in_path="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/aligned_genomic_reads/aligned_genomic_reads.sam"
sam_out_path="/Users/manuel/Desktop"
file_name="out_bc_umi.sam"


python3 $scripts/add_BC_UMI_tags.py \
     --bc_in $path_to_bc \
     --umi_in $path_to_umi \
     --sam_in $sam_in_path \
     --sam_out $sam_out_path \
     --file_name $file_name
