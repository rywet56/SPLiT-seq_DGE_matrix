#!/usr/bin/env bash

#$ -l h_rt=02:00:00
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 8
#$ -m ea

bowtie2_index="/fast/AG_Ohler/manuel/che_wei_data/10X_bc_index/10X_bc_index"
cbc_reads="/fast/AG_Ohler/manuel/che_wei_data/data_2/extracted_cbcs.fastq"
output="/fast/AG_Ohler/manuel/che_wei_data/data_2/align_cbcs_ordered.sam"

bowtie2 \
     -p 8 \
     -x $bowtie2_index \
     -U $cbc_reads \
     -S $output \
     --reorder

# --reorder --> arragnes the aligned reads in the same order as in the input file

# bowtie2 automatically only outputs the best alignment if a read aligns multiple times. Thats why there is not HI tag.
