#!/usr/bin/env bash


ANNOTATED_GENOME="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/genome/annotated_genome"
GENOME="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/genome/mm_GRCm38.75.fasta"
GTF="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/genome/mm_GRCm38.75.gtf"

STAR \
     --runThreadN 4 \
     --runMode genomeGenerate \
     --genomeDir $ANNOTATED_GENOME \
     --genomeFastaFiles $GENOME \
     --sjdbGTFfile $GTF \
     --sjdbOverhang 100-1

