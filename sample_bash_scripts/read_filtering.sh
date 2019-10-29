#!/usr/bin/env bash

#meta_data="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata"
#scripts=$(pwd)
#
#in1=$meta_data/barcodes_paper/R1_barcodes.txt
#out1=$meta_data/barcodes_paper
#name1="r1barcodes"
#
#python3 $scripts/extract_barcodes_txt_to_FASTA.py --in_dir $in1 --out_dir $out1 --file_name $name1
#
#
#in2=$meta_data/barcodes_paper/R2_barcodes.txt
#out2=$meta_data/barcodes_paper
#name2="r2barcodes"
#
#python3 $scripts/extract_barcodes_txt_to_FASTA.py --in_dir $in2 --out_dir $out2 --file_name $name2
#
#in3=$meta_data/barcodes_paper/R3_barcodes.txt
#out3=$meta_data/barcodes_paper
#name3="r3barcodes"
#
#python3 $scripts/extract_barcodes_txt_to_FASTA.py --in_dir $in3 --out_dir $out3 --file_name $name3

# export PATH="$PATH:/usr/local/bin/python"

# -------------------------------------------------------------- #

#meta_data="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata"
#scripts=$(pwd)
#
#bc_ref=$meta_data/barcode_reference/barcode_combinations.fasta
#bc_reads=$meta_data/barcode_reads/extracted_barcodes_500.txt
#out_dir=$meta_data/results
#
#python3 $scripts/align_per_list_element.py \
#    --bc_reference $bc_ref \
#    --bc_reads $bc_reads \
#    --out_dir $out_dir

# -------------------------------------------------------------- #

#meta_data="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata"
#scripts=$(pwd)
#
#bc_ref=$meta_data/barcode_reference/barcode_combinations.txt
#bc_reads=$meta_data/barcode_reads/extracted_barcodes_500.txt
#gen_reads=$meta_data/barcode_reads/test_500.fastq
#out_dir=$meta_data/results
#
#python3 $scripts/filter_barcodes.py \
#    --bc_reference $bc_ref \
#    --bc_reads $bc_reads \
#    --gen_reads $gen_reads \
#    --out_dir $out_dir

# -------------------------------------------------------------- #

meta_data="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata"
scripts="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix"

bc_ref=$meta_data/barcode_reference/barcode_combinations.txt
bc_reads=$meta_data/barcode_reads/test_500.fastq
gen_reads=$meta_data/barcode_reads/test_500.fastq
out_dir=$meta_data/results

python3 $scripts/filter_barcodes_advanced.py \
    --bc_reference $bc_ref \
    --bc_reads $bc_reads \
    --gen_reads $gen_reads \
    --out_dir $out_dir \
    --mode "simple"

# -------------------------------------------------------------- #
