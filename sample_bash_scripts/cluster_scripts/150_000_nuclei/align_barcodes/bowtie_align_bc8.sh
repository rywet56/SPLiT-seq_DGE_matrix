#!/usr/bin/env bash

#$ -l h_rt=00:30:00 -l h_vmem=10G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt
#$ -pe smp 8
#$ -m ea


metadata="/fast/AG_Ohler/manuel/splitseq/metadata"

bowtie2_index=$metadata/bc_index_files/bc_index
barcodes="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/extracted_cbcs_umis/extracted_cbcs_b8.fastq"
output="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/aligned_cbs/aligned_cbcs_b8.sam"

bowtie2 \
     -p 8 \
     -x $bowtie2_index \
     -U $barcodes \
     -S $output
