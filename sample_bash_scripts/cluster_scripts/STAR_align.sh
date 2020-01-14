#!/usr/bin/env bash

#$ -l h_rt=10:00:00 -l h_vmem=80G
#$ -o /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/aligned_sel_genes_2/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/aligned_sel_genes_2/err_file.txt
#$ -pe smp 8


INPUT_fastq="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/selected_cbcs_umis_genes/selected_gens.fastq"
ANNOTATED_GENOME="/fast/AG_Ohler/manuel/splitseq/mus_musculus_metadata_mm10/annotated_genome_sjdbO_65"
out_dir="/fast/AG_Ohler/manuel/splitseq/frozen_preserved_cells_nuclei_200_UBCs/aligned_sel_genes/aligned_sel_genes_2"


STAR \
     --runThreadN 8 \
     --genomeDir $ANNOTATED_GENOME \
     --readFilesIn $INPUT_fastq \
     --outFileNamePrefix $out_dir \
     --outSAMunmapped Within \
     --outFilterScoreMinOverLread 0.33 \
     --outFilterMatchNminOverLread 0.33
     
#--outSAMorder PairedKeepInputOrder

