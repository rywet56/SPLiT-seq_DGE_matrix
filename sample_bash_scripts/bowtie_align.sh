#!/usr/bin/env bash

#$ -l h_rt=00:03:00
#$ -o /fast/AG_Ohler/manuel/splitseq/bowtie_align_output_file
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/bowtie_align_err_file
#$ -pe smp 8

HOME="/fast/AG_Ohler/manuel/splitseq"
bowtie2_index=$HOME/bowtie2_index/mus_musculus
genomic_reads=$HOME/filtered_genomic_reads.fastq
output=$HOME/bowtie_aligned_reads.sam

bowtie2 \
     -p 8 \
     -x "/fast/AG_Ohler/manuel/splitseq/bowtie2_index/mus_musculus" \
     -U $genomic_reads \
     -S $output
