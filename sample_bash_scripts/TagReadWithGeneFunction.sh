#!/usr/bin/env bash

dropseq_tools="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix/sample_bash_scripts/drop_seq_tools"
#aligned="/Users/manuel/Desktop/aligned_filtered_genomic_reads_8mio.sam"
aligned="/Users/manuel/Desktop/bowtie_strategy/aligned_filtered_genomic_reads.sam"
#out="/Users/manuel/Desktop/genfun_tagged.sam"
out="/Users/manuel/Desktop/bowtie_strategy/genfun_tagged.sam"
META_DATA="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/sample_data/mm10_genome/genome_annotation/mm10.refFlat"

$dropseq_tools/TagReadWithGeneFunction \
     I=$aligned \
     O=$out \
     ANNOTATIONS_FILE=$META_DATA
