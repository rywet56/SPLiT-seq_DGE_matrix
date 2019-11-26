#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=20G
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 2

home_dir="/fast/AG_Ohler/manuel/splitseq"
scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

bc_reads="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/SRR6750059_2.fastq"
output="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs"
umi_out_name="extracted_umis"
cbc_out_name="extracted_cbcs"

python3 $scripts/extract_cbc_umi.py \
    --bc_reads $bc_reads \
    --out_dir $output \
    --cbc_out_name "extracted_cbcs" \
    --umi_out_name "extracted_umis"




