#!/usr/bin/env bash

bowtie2_index="/Users/manuel/Desktop/bowtie_strategy/bc_index_files/bc_index"
genomic_reads="/Users/manuel/Desktop/bowtie_strategy/extracted_bcs.fastq"
output="/Users/manuel/Desktop/bowtie_strategy/aligned_bcs.sam"

bowtie2 \
     -p 4 \
     -x $bowtie2_index \
     -U $genomic_reads \
     -S $output
