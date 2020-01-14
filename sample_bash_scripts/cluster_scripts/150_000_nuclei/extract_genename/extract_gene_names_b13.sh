#!/usr/bin/env bash

#$ -l h_rt=02:00:00 -l h_vmem=310G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

sam_file="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/genes/gen_tagged_b13.sam"
out="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/genes"
name="sorted_gene_names_b13"

python3 $scripts/extract_gene_name.py \
    --sam_in $sam_file \
    --out_dir $out \
    --file_name $name \
    --accepted_gf "CODING,UTR,INTERGENIC,INTRONIC"
