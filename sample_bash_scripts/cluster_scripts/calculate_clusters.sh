#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=60G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"


barcode_clusters="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/clustered_bcs/clustered_barcodes.txt"
umi_clusters="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/clustered_umis/clustered_umis.txt"
genes="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/extracted_gene_names/sorted_gene_names.txt"
out="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/clusters"
name="cluster_out"

python3 $scripts/calculate_clusters.py \
    --cbc_clusters $barcode_clusters \
    --umi_clusters $umi_clusters \
    --gene_names $genes \
    --out_dir $out \
    --file_name $name
