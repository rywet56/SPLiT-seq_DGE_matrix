#!/usr/bin/env bash

dropseq_tools="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix/sample_bash_scripts/drop_seq_tools"
genfun_tagged="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix/sample_raw_data/genfunc_sorted_tagged_filtered_aligned_genomic_reads/genfun_tagged.sam"
out="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix/sample_raw_data/DGE_matrix/sample_dge_matrix.dge"
summary="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix/sample_raw_data/DGE_matrix/sample_dge_matrix_summary.txt"

$dropseq_tools/DigitalExpression \
     I=$genfun_tagged \
     O=$out \
     SUMMARY=$summary \
     NUM_CORE_BARCODES=100
