#!/usr/bin/env bash

meta_data="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata"
scripts="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix"
#
#
## create a .txt file each of R1 - R3 barcodes
#in1=$meta_data/barcodes_paper/R1_barcodes.txt
#out1=$meta_data/barcodes_paper
#name1="r1barcodes"
#
#python3 $scripts/barcodes_to_txt.py \
#    --in_dir $in1 \
#    --out_dir $out1 \
#    --file_name $name1
#
#
#in2=$meta_data/barcodes_paper/R2_barcodes.txt
#out2=$meta_data/barcodes_paper
#name2="r2barcodes"
#
#python3 $scripts/barcodes_to_txt.py \
#    --in_dir $in2 \
#    --out_dir $out2 \
#    --file_name $name2
#
#in3=$meta_data/barcodes_paper/R3_barcodes.txt
#out3=$meta_data/barcodes_paper
#name3="r3barcodes"
#
#python3 $scripts/barcodes_to_txt.py \
#    --in_dir $in3 \
#    --out_dir $out3 \
#    --file_name $name3



# create one .txt file that contains all possible combinations of R1-R3 barcodes
bc1=$meta_data/barcodes_paper/r1barcodes.txt
bc2=$meta_data/barcodes_paper/r2barcodes.txt
bc3=$meta_data/barcodes_paper/r3barcodes.txt
out=$meta_data/barcode_reference

python3 $scripts/create_bc_comb.py \
    --bc1 $bc1 \
    --bc2 $bc2 \
    --bc3 $bc3 \
    --out_dir $out
