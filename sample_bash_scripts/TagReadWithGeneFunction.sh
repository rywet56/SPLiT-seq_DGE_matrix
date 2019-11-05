#!/usr/bin/env bash

dropseq_tools="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix/sample_bash_scripts/drop_seq_tools"
tagged_aligned="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix/sample_raw_data/sorted_tagged_aligned_filtered_genomic_reads/out_bc_umi.sam"
out="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix/sample_raw_data/genfunc_sorted_tagged_filtered_aligned_genomic_reads/genfun_tagged.sam"
META_DATA="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix/sample_raw_data/genome_annotation/mm10.refFlat"

$dropseq_tools/TagReadWithGeneFunction \
     I=$tagged_aligned \
     O=$out \
     ANNOTATIONS_FILE=$META_DATA
