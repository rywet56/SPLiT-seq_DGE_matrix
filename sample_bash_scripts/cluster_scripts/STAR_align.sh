#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=20G
#$ -o /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/err_file.txt
#$ -pe smp 8

HOME_Dir="/fast/AG_Ohler/manuel/splitseq"
INPUT_fastq=$HOME_Dir/frozen_preserved_cells_nuclei_200_UBCs/SRR6750059_1.fastq
ANNOTATED_GENOME=$HOME_Dir/mus_musculus_metadata_mm10/annotated_genome

STAR \
     --runThreadN 8 \
     --genomeDir $ANNOTATED_GENOME \
     --readFilesIn $INPUT_fastq \
     --outFileNamePrefix star_aligned

