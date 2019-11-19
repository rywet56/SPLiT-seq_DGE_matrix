#!/usr/bin/env bash

meta_data=""
scripts="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix"


barcode_clusters="/Users/manuel/Desktop/clustered_barcodes.txt"
umi_clusters="/Users/manuel/Desktop/clustered_UMIs.txt"
genes="/Users/manuel/Desktop/sorted_gene_names.txt"
out="/Users/manuel/Desktop"
name="cluster_out"

python3 $scripts/calculate_clusters.py \
    --cbc_clusters $barcode_clusters \
    --umi_clusters $umi_clusters \
    --gene_names $genes \
    --out_dir $out \
    --file_name $name
