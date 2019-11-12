#!/usr/bin/env bash

f1="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/file1.fastq"
f2="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/file2.fastq"
f3="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/file3.fastq"
f4="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/file4.fastq"

input_files="$f1;$f2;$f3;$f4"

echo $input_files

scripts="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix"
out_directory="/Users/manuel/Desktop"
file_name="merged_reads"


python3 $scripts/merge_fastq.py \
     --in_dir $input_files \
     --out_dir $out_directory \
     --file_name $file_name
