#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=50G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 1
#$ -m ea

bowtie2_index="/fast/AG_Ohler/manuel/splitseq/metadata/bc_index_files/bc_index"
cbc_reads="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/extracted_cbcs_128M_stack.fastq"
output="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/aligned_cbcs.sam"

bowtie2 \
     -p 8 \
     -x $bowtie2_index \
     -U $cbc_reads \
     -S $output
