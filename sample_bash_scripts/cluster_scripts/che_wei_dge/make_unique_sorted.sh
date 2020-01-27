#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=600G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

sam_in_path="/fast/AG_Ohler/manuel/che_wei_data/data_2/genfun_tagged_not_unique.sam"
sam_out_path="/fast/AG_Ohler/manuel/che_wei_data/data_2"
file_name="genfun_tagged_unique.sam"


python3 $scripts/make_unique_ordered.py \
     --sam_in $sam_in_path \
     --sam_out $sam_out_path \
     --file_name $file_name
