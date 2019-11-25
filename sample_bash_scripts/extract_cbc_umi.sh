#!/usr/bin/env bash

scripts="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix"

bc_reads="/Users/manuel/Desktop/bowtie_strategy/SRR6750059_2_1mio.fastq"
output="/Users/manuel/Desktop/bowtie_strategy"
umi_out_name="extracted_umis"
cbc_out_name="extracted_cbcs"

python3 $scripts/extract_cbc_umi.py \
    --bc_reads $bc_reads \
    --out_dir $output \
    --cbc_out_name $cbc_out_name \
    --umi_out_name $umi_out_name
