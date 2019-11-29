#!/usr/bin/env bash

bowtie2_index="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/sample_data/mm10_genome/genome_index/mus_musculus"
genomic_reads="/Users/manuel/Desktop/SRR6750059_1_1mio.fastq"
#genomic_reads="/Users/manuel/Desktop/bowtie_strategy/selected_gens.fastq"
output="/Users/manuel/Desktop/bowtie_strategy/aligned_filtered_genomic_reads.sam"

bowtie2 \
     -p 4 \
     -x $bowtie2_index \
     -U $genomic_reads \
     -S $output
