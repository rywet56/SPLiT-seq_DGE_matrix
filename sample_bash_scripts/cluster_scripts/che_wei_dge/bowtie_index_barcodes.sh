#!/usr/bin/env bash

genome="/Users/manuel/Desktop/10X_bc_combinations.fasta"
out="/Users/manuel/Desktop/10X_bc_index/10X_bc_index"

bowtie2-build \
     --threads 4 \
     $genome \
     $out
