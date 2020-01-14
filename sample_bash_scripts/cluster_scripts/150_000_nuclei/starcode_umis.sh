#!/usr/bin/env bash

#$ -l h_rt=20:00:00
#$ -o /fast/AG_Ohler/manuel/splitseq/150000_nuclei/out_r5.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/150000_nuclei/err_r5.txt
#$ -pe smp 8
#$ -m ea

inp="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/sel_reads/sel_umis_2.txt"

out="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/clustered_umis_d2_r5.txt"

starcode \
     --threads 8 \
     --input $inp \
     --output $out \
     -d 2 \
     -r 5 \
     --seq-id
     
#     --print-clusters
