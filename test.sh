#!/usr/bin/env bash

#home_dir=$(pwd)

#in1=$home_dir/barcodes/R1_barcodes.txt
#out1=$home_dir
#name1="r1barcodes"
#python3 $home_dir/barcodes_txt_to_FASTA.py --indir $in1 --outdir $out1 --outfilename $name1
#
#
#in2=$home_dir/barcodes/R2_barcodes.txt
#out2=$home_dir
#name2="r2barcodes"
#python3 $home_dir/barcodes_txt_to_FASTA.py --indir $in2 --outdir $out2 --outfilename $name2
#
#
#in3=$home_dir/barcodes/R3_barcodes.txt
#out3=$home_dir
#name3="r3barcodes"
#python3 $home_dir/barcodes_txt_to_FASTA.py --indir $in3 --outdir $out3 --outfilename $name3

# export PATH="$PATH:/usr/local/bin/python"

# -------------------------------------------------------------- #

meta_data="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata"
scripts=$(pwd)

bc_ref=$meta_data/barcode_reference/barcode_combinations.fasta
bc_reads=$meta_data/barcode_reads/extracted_barcodes_1000000.txt
out_dir=$meta_data/results

python3 $scripts/align_per_list_element.py \
    --bc_reference $bc_ref \
    --bc_reads $bc_reads \
    --out_dir $out_dir

# -------------------------------------------------------------- #


