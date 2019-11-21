#!/usr/bin/env bash

#$ -l h_rt=10:00:00
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 1

home_dir="/fast/AG_Ohler/manuel/splitseq"
scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"
metadata="/fast/AG_Ohler/manuel/splitseq/metadata"

bowtie2_index=$metadata/bc_index_files/bc_index
barcode="/Users/manuel/Desktop/filtered_genomic_reads_1mio.fastq"
output="/Users/manuel/Desktop/aligned_filtered_genomic_reads_1mio.sam"

python3 $scripts/extract_cbc_umi.py
