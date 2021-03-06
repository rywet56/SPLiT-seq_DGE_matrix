#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=10G
#$ -o /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/aligned_sel_genes_2/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/aligned_sel_genes_2/err_file.txt
#$ -pe smp 8

ANNOTATED_GENOME="/fast/AG_Ohler/manuel/splitseq/mus_musculus_metadata_mm10/annotated_genome_sjdbO_65"
GENOME="/fast/AG_Ohler/manuel/splitseq/mus_musculus_metadata_mm10/mm10.fasta"
GTF="/fast/AG_Ohler/manuel/splitseq/mus_musculus_metadata_mm10/mm10.gtf"

STAR \
     --runThreadN 8 \
     --runMode genomeGenerate \
     --genomeDir $ANNOTATED_GENOME \
     --genomeFastaFiles $GENOME \
     --sjdbGTFfile $GTF \
     --sjdbOverhang 65

