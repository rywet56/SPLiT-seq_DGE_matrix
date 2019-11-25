#!/usr/bin/env bash

dropseq_tools="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix/sample_bash_scripts/drop_seq_tools"
genfun_tagged="/Users/manuel/Desktop/bowtie_strategy/drop_seq_dge_matrix/out_bc_umi.sam"
out="/Users/manuel/Desktop/bowtie_strategy/drop_seq_dge_matrix/sample_dge_matrix.txt"
summary="/Users/manuel/Desktop/bowtie_strategy/drop_seq_dge_matrix/sample_dge_matrix_summary.txt"

$dropseq_tools/DigitalExpression \
     I=$genfun_tagged \
     O=$out \
     SUMMARY=$summary \
     READ_MQ=-500 \
     STRAND_STRATEGY=BOTH \
     NUM_CORE_BARCODES=6115


