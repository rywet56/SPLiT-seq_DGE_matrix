#!/usr/bin/env bash

#$ -l h_rt=3:00:00 -l h_vmem=10G
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_3.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_3.txt
#$ -pe smp 1

tool="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix/sample_bash_scripts/cluster_scripts/che_wei_dge"
gtf_file="/fast/AG_Ohler/manuel/che_wei_data/data_2/thaliana_gtf/at.gtf"
refflat_out="/fast/AG_Ohler/manuel/che_wei_data/data_2/annotation.refFlat"

$tool/gtfToGenePred.dms \
    $gtf_file \
    $refflat_out
