#!/usr/bin/env bash

#$ -l h_rt=4:00:00 -l h_vmem=310G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

home_dir="/fast/AG_Ohler/manuel/splitseq"
scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

sam_file="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/nametagged_aligned_sel_genes/genfun_tagged.sam"
out="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/extracted_gene_names"
name="sorted_gene_names"

python3 $scripts/extract_gene_name.py \
    --sam_in $sam_file \
    --out_dir $out \
    --file_name $name \
    --accepted_gf "CODING,UTR,INTERGENIC,INTRONIC"
