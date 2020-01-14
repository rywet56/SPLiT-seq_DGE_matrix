#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=1G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

bc_reads="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/batch_3/SRR6750044_2.fastq"
output="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/extracted_cbcs_umis"
umi_out_name="extracted_umis_b3"
cbc_out_name="extracted_cbcs_b3"

python3 $scripts/extract_cbc_umi.py \
    --bc_reads $bc_reads \
    --out_dir $output \
    --cbc_out_name $cbc_out_name \
    --umi_out_name $umi_out_name
    
    




