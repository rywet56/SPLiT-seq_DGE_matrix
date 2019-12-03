#!/usr/bin/env bash

#$ -l h_rt=01:00:00 -l h_vmem=20G
#$ -o /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/err_file.txt
#$ -pe smp 8

HOME_Dir="/fast/AG_Ohler/manuel/splitseq"
INPUT_fastq=$HOME_Dir/frozen_preserved_cells_nuclei_200_UBCs/selected_gens.fastq
ANNOTATED_GENOME=$HOME_Dir/mus_musculus_metadata_mm10/annotated_genome

STAR \
     --runThreadN 8 \
     --genomeDir $ANNOTATED_GENOME \
     --readFilesIn $INPUT_fastq \
     --outFileNamePrefix $HOME_Dir/frozen_preserved_cells_nuclei_200_UBCs/star_aligned/star_aligned \
     --outSAMunmapped Within \
     --outFilterScoreMinOverLread 0.33 \
     --outFilterMatchNminOverLread 0.33
     
#--outSAMorder PairedKeepInputOrder

