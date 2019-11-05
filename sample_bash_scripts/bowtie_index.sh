#!/usr/bin/env bash

#$ -l h_rt=02:00:00
#$ -o /fast/AG_Ohler/manuel/splitseq/bowtie_output_file
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/bowtie_err_file
#$ -pe smp 8

HOME="/fast/AG_Ohler/manuel/splitseq"
genome=$HOME/mus_musculus_metadata_mm10/mm10.fasta
out=$HOME/bowtie2_index/mus_musculus

bowtie2-build \
     --threads 8 \
     $genome \
     $out
