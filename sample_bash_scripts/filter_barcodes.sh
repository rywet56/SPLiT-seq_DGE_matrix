#!/usr/bin/env bash

#$ -l h_rt=03:00:00
#$ -l h_vmem=60G
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file
#$ -pe smp 1

meta_data="/fast/AG_Ohler/manuel/splitseq/150000_nuclei"
scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

bc_ref=$meta_data/barcode_combinations.txt
#bc_reads=$meta_data/SRR6750042_2.fastq
#gen_reads=$meta_data/SRR6750042_1.fastq
bc_reads=$meta_data/bc_4000000.fastq
gen_reads=$meta_data/gen_4000000.fastq
out_dir=$meta_data

python3 $scripts/filter_barcodes_advanced.py \
    --bc_reference $bc_ref \
    --bc_reads $bc_reads \
    --gen_reads $gen_reads \
    --out_dir $out_dir
