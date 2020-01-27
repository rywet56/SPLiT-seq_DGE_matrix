#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=360G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_2.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_2.txt
#$ -pe smp 1
#$ -m ea

picard_tools="/fast/AG_Ohler/manuel/splitseq/picard_tools/picard.jar"
reference_genome="/fast/AG_Ohler/manuel/che_wei_data/data_2/thaliana_fasta/at_complete.fasta"
#out="/fast/AG_Ohler/manuel/che_wei_data/data_2/seq_dic"

java -jar $picard_tools CreateSequenceDictionary \
    REFERENCE=$reference_genome
#    O=$out

