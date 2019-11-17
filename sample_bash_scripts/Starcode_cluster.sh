#!/usr/bin/env bash

inp="/Users/manuel/Desktop/filtered_bc_reads_2.txt"
out="/Users/manuel/Desktop/clustered_barcodes_test"

starcode \
     --threads 2 \
     --input $inp \
     --output $out \
     -d 4 \
     -r 1 \
     --seq-id 
#     --print-clusters


