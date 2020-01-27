#!/usr/bin/env bash

#$ -l h_rt=7:00:00 -l h_vmem=370G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 1
#$ -m ea

drop_seq_tools="/fast/AG_Ohler/manuel/drop_seq/Drop_seq_tools"
sam_in="/fast/AG_Ohler/manuel/che_wei_data/data_2/bc_umi_gene_tagged.sam"
dge_out="/fast/AG_Ohler/manuel/che_wei_data/data_2/dge.txt"
dge_summary="/fast/AG_Ohler/manuel/che_wei_data/data_2/dge_summary.txt"

$drop_seq_tools/DigitalExpression \
     I=$sam_in \
     O=$dge_out \
     SUMMARY=$dge_summary \
     NUM_CORE_BARCODES=10000000
