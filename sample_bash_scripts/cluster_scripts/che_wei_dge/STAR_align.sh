#!/usr/bin/env bash

#$ -l h_rt=20:00:00 -l h_vmem=800G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 1
#$ -m ea


INPUT_fastq="/fast/AG_Ohler/manuel/che_wei_data/data_2/selected_gens.fastq"
ANNOTATED_GENOME="/fast/AG_Ohler/manuel/che_wei_data/data_2/thaliana_star_index"
out_dir="/fast/AG_Ohler/manuel/che_wei_data/data_2/star_aligned_gen_reads/aligned_sel_genes"


STAR \
     --runThreadN 8 \
     --genomeDir $ANNOTATED_GENOME \
     --readFilesIn $INPUT_fastq \
     --outFileNamePrefix $out_dir \
     --outSAMunmapped Within \
     --outFilterScoreMinOverLread 0.66 \
     --outFilterMatchNminOverLread 0.66 \
     --outSAMorder PairedKeepInputOrder

#--outSAMunmapped Within \  # ensure that reads that could not be mapped are listed
#--outSAMorder PairedKeepInputOrder  # output aligned reads ordered by coordinate
