#!/usr/bin/env bash

#$ -l h_rt=02:00:00 -l h_vmem=20G
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 1

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

python3 $scripts/test_import.py




