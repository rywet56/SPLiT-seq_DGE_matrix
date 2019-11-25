#!/usr/bin/env bash

meta_data=""
scripts="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix"


#sam_file="/Users/manuel/Desktop/genfun_tagged.sam"
sam_file="/Users/manuel/Desktop/bowtie_strategy/genfun_tagged.sam"
#out="/Users/manuel/Desktop"
out="/Users/manuel/Desktop/bowtie_strategy"
name="sorted_gene_names"

python3 $scripts/extract_gene_name.py \
    --sam_in $sam_file \
    --out_dir $out \
    --file_name $name
