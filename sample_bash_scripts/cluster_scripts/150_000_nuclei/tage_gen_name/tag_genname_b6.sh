#!/usr/bin/env bash

#$ -l h_rt=2:00:00 -l h_vmem=10G
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 1
#$ -m ea

dropseq_tools="/fast/AG_Ohler/manuel/splitseq/dropseq_tools"
aligned="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/genes/aligned_genes_b6.samAligned.out.sam"
out="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/genes/gen_tagged_b6.sam"
META_DATA="/fast/AG_Ohler/manuel/splitseq/mus_musculus_metadata_mm10/mm10.refFlat"

$dropseq_tools/TagReadWithGeneFunction \
     I=$aligned \
     O=$out \
     ANNOTATIONS_FILE=$META_DATA
