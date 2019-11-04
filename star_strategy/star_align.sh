#!/usr/bin/env bash

HOME_dic="/Users/manuel/Desktop/test"
ANNOTATED_GENOME=$HOME_dic/annot_genome_small
INPUT_fastq=$HOME_dic/barcodes_notworking.fasta

STAR \
     --runThreadN 1 \
     --genomeDir $ANNOTATED_GENOME \
     --readFilesIn $INPUT_fastq \
     --outFileNamePrefix guliguli \
     --outSAMattributes All
