#!/usr/bin/env bash

#$ -l h_rt=20:00:00 -l h_vmem=800G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix/sample_bash_scripts/cluster_scripts/che_wei_dge/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix/sample_bash_scripts/cluster_scripts/che_wei_dge/err_file.txt
#$ -pe smp 1

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

path_to_bc="/fast/AG_Ohler/manuel/che_wei_data/data_2/selected_barcodes.txt"
path_to_umi="/fast/AG_Ohler/manuel/che_wei_data/data_2/selected_umis.txt"
sam_in_path="/fast/AG_Ohler/manuel/che_wei_data/data_2/genfun_tagged_unique.sam"
sam_out_path="/fast/AG_Ohler/manuel/che_wei_data/data_2"
file_name="bc_umi_gene_tagged.sam"


python3 $scripts/add_BC_UMI_tags.py \
     --bc_in $path_to_bc \
     --umi_in $path_to_umi \
     --sam_in $sam_in_path \
     --sam_out $sam_out_path \
     --file_name $file_name
