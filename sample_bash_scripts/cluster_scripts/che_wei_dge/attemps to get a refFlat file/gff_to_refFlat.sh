#!/usr/bin/env bash

#$ -l h_rt=3:00:00 -l h_vmem=10G
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file_3.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file_3.txt
#$ -pe smp 1

tool="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix/sample_bash_scripts/cluster_scripts/che_wei_dge"
gff_file="/fast/AG_Ohler/manuel/che_wei_data/data_2/TAIR10_GFF3_genes.gff"
refflat_out="/fast/AG_Ohler/manuel/che_wei_data/data_2/annotation.refFlat"

$tool/gff3ToGenePred.dms \
    $gff_file \
    $refflat_out
