#!/usr/bin/env bash

#$ -l h_rt=3:00:00 -l h_vmem=10G
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_1.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_1.txt
#$ -pe smp 1

#dropseq_tools="/fast/AG_Ohler/manuel/splitseq/dropseq_tools"
dropseq_tools="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix/sample_bash_scripts/cluster_scripts/che_wei_dge/Drop-seq_tools-2.3.0"
out="/fast/AG_Ohler/manuel/che_wei_data/data_2/reduced.gtf
gtf="/fast/AG_Ohler/manuel/che_wei_data/data_2/Arabidopsis_thaliana.TAIR10.46.gtf"
dic="/fast/AG_Ohler/manuel/che_wei_data/data_2/thaliana_fasta/at_complete.dict"

$dropseq_tools/ReduceGTF \
     SEQUENCE_DICTIONARY=$dic \
     GTF=$gtf \
     OUTPUT=my.reduced.gtf
