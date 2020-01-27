#!/usr/bin/env bash

#$ -l h_rt=3:00:00 -l h_vmem=10G
#$ -o /fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix/sample_bash_scripts/cluster_scripts/che_wei_dge/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix/sample_bash_scripts/cluster_scripts/che_wei_dge/err_file.txt
#$ -pe smp 1

#dropseq_tools="/fast/AG_Ohler/manuel/splitseq/dropseq_tools"
dropseq_tools="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix/sample_bash_scripts/cluster_scripts/che_wei_dge/Drop-seq_tools-2.3.0"
aligned=
out="/fast/AG_Ohler/manuel/che_wei_data/data_2/genfun_tagged.sam"
META_DATA="/fast/AG_Ohler/manuel/che_wei_data/data_2/AT_modified_2.gtf"

$dropseq_tools/TagReadWithGeneFunction \
     I=$aligned \
     O=$out \
     ANNOTATIONS_FILE=$META_DATA
