#!/usr/bin/env bash

#$ -l h_rt=02:00:00
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 8
#$ -m ea

bowtie2_index="/fast/AG_Ohler/manuel/splitseq/metadata/bc_index_files/bc_index"
cbc_reads="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/extracted_cbcs.fastq"
output="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/align_cbcs_ordered.sam"

bowtie2 \
     -p 8 \
     -x $bowtie2_index \
     -U $cbc_reads \
     -S $output \
     --reorder

# --reorder --> arragnes the aligned reads in the same order as in the input file
