#!/usr/bin/env bash

#$ -l h_rt=10:00:00
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 8

home_dir="/fast/AG_Ohler/manuel/splitseq"
scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix/sample_bash_scripts"
metadata="/fast/AG_Ohler/manuel/splitseq/metadata"

bowtie2_index=$metadata/bc_index_files/bc_index
barcodes="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/extracted_bcs.fastq"
output="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/aligned_barcodes.sam"

bowtie2 \
     -p 8 \
     -x $bowtie2_index \
     -U $barcodes \
     -S $output
