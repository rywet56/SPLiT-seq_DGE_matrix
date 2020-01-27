#!/usr/bin/env bash

#$ -l h_rt=3:00:00 -l h_vmem=10G
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_3.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_3.txt
#$ -pe smp 1

dropseq_tools="/fast/AG_Ohler/manuel/splitseq/dropseq_tools"
gtf_file="/fast/AG_Ohler/manuel/che_wei_data/data_2/thaliana_gtf/at.gtf"
seq_dic="/fast/AG_Ohler/manuel/che_wei_data/data_2/thaliana_fasta/at_complete.dict"
refflat_out="/fast/AG_Ohler/manuel/che_wei_data/data_2/annotation.refFlat"

$dropseq_tools/ConvertToRefFlat \
    ANNOTATIONS_FILE=$gtf_file \
    SEQUENCE_DICTIONARY=$seq_dic  \
    O=$refflat_out
