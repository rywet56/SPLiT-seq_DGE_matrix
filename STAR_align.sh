#!/usr/bin/env bash

HOME_Drop_Seq="/fast/AG_Ohler/manuel/drop_seq"
INPUT_fastq=$HOME_Drop_Seq/unaligned_mc_tagged_polyA_filtered.fastq
ANNOTATED_GENOME=$HOME_Drop_Seq/mm10/annotated_genome

STAR \
     --runThreadN 8 \
     --genomeDir $ANNOTATED_GENOME \
     --readFilesIn $INPUT_fastq \
     --outFileNamePrefix star \

conda deactivate
