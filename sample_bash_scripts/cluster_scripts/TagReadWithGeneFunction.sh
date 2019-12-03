#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=320G
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 1

dropseq_tools="/fast/AG_Ohler/manuel/splitseq/dropseq_tools"
aligned="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/star_alignedAligned.out.sam"
out="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/genfun_tagged.sam"
META_DATA="/fast/AG_Ohler/manuel/splitseq/mus_musculus_metadata_mm10/mm10.refFlat"

$dropseq_tools/TagReadWithGeneFunction \
     I=$aligned \
     O=$out \
     ANNOTATIONS_FILE=$META_DATA
