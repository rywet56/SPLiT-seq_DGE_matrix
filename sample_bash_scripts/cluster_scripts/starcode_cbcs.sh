#!/usr/bin/env bash

#$ -l h_rt=05:00:00 -l h_vmem=20G
#$ -o /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/clustered_bcs/out.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/clustered_bcs/err.txt
#$ -pe smp 1
#$ -m ea

inp="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/selected_cbcs_umis_genes/selected_barcodes.txt"

out="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/clustered_bcs/clustered_barcodes.txt"

starcode \
     --threads 8 \
     --input $inp \
     --output $out \
     -d 1 \
     -r 1 \
     --seq-id
     
#     --print-clusters
