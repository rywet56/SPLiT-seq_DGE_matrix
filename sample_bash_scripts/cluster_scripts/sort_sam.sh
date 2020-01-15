#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=360G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

picard_tools="/fast/AG_Ohler/manuel/splitseq/picard_tools/picard.jar"

java -jar $picard_tools SortSam \
    I="/Users/manuel/Desktop/aligned_gen_reads_10.sam" \
    O="/Users/manuel/Desktop/sorted.sam" \
    SORT_ORDER=coordinate
