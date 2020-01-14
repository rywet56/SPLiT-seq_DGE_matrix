#!/usr/bin/env bash

#$ -l h_rt=02:00:00
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 8
#$ -m ea


INPUT_fastq="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/sel_reads/selected_gens_b10.fastq"
ANNOTATED_GENOME="/fast/AG_Ohler/manuel/splitseq/mus_musculus_metadata_mm10/annotated_genome_sjdbO_65"
out_dir="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/genes/aligned_genes_b10.sam"


STAR \
     --runThreadN 8 \
     --genomeDir $ANNOTATED_GENOME \
     --readFilesIn $INPUT_fastq \
     --outFileNamePrefix $out_dir \
     --outSAMunmapped Within \
     --outFilterScoreMinOverLread 0.66 \
     --outFilterMatchNminOverLread 0.66
     
#--outSAMorder PairedKeepInputOrder

