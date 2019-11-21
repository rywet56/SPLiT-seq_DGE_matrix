#!/usr/bin/env bash

genome=/Users/manuel/Desktop/bowtie_strategy/barcode_combinations.fasta
out=/Users/manuel/Desktop/bowtie_strategy/bc_index_files/bc_index

bowtie2-build \
     --threads 4 \
     $genome \
     $out
