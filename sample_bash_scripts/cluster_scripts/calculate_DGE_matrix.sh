#!/usr/bin/env bash

#$ -l h_rt=01:00:00 -l h_vmem=60G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

clusters="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/clusters/test_10.txt"
out="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/dge_matrix"

name="expression_new_10"

python3 $scripts/calculate_DGE_matrix.py \
    --clusters $clusters \
    --out_dir $out \
    --file_name $name
