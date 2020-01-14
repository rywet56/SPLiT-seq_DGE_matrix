#!/usr/bin/env bash

#$ -l h_rt=20:00:00
#$ -o /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/clustered_bcs/out.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/clustered_bcs/err.txt
#$ -pe smp 8
#$ -m ea

inp="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/sel_reads/sel_barcodes_2.txt"

out="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/clustered_barcodes_2.txt"

starcode \
     --threads 8 \
     --input $inp \
     --output $out \
     -d 1 \
     -r 1 \
     --seq-id
     
#     --print-clusters
