#!/usr/bin/env bash

HOME_dic="/Users/manuel/Desktop/test"
ANNOTATED_GENOME=$HOME_dic/annot_genome_small
GENOME=$HOME_dic/barcodes.fasta

STAR \
     --runThreadN 1 \
     --runMode genomeGenerate \
     --genomeDir $ANNOTATED_GENOME \
     --genomeFastaFiles $GENOME \
     --genomeSAindexNbases 1
