#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=360G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"


barcode_clusters="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/clustered_barcodes.txt"
umi_clusters="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/clustered_umis_d2.txt"
genes="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/genes/sel_genes.txt"
out="/fast/AG_Ohler/manuel/splitseq/150000_nuclei"
name="calculated_clusters_umisd2"

python3 $scripts/calculate_clusters.py \
    --cbc_clusters $barcode_clusters \
    --umi_clusters $umi_clusters \
    --gene_names $genes \
    --out_dir $out \
    --file_name $name
