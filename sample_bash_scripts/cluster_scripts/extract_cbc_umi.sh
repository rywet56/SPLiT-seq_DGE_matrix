#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=370G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

home_dir="/fast/AG_Ohler/manuel/splitseq"
scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

bc_reads="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/SRR6750059_2_second_part.fastq"
output="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs"
umi_out_name="extracted_umis_128M_stack_secondpart"
cbc_out_name="extracted_cbcs_128M_stack_secondpart"

python3 $scripts/extract_cbc_umi.py \
    --bc_reads $bc_reads \
    --out_dir $output \
    --cbc_out_name $cbc_out_name \
    --umi_out_name $umi_out_name




