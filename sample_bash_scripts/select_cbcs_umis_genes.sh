#!/usr/bin/env bash

scripts="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/SPLiT-seq_DGE_matrix"

path_to_cbcs_sam="/Users/manuel/Desktop/bowtie_strategy/aligned_bcs.sam"
path_to_bc_comb="/Users/manuel/Desktop/bowtie_strategy/barcode_combinations.fasta"
path_to_umis_fastq="/Users/manuel/Desktop/bowtie_strategy/extracted_umis.fastq"
path_to_gen_fastq="/Users/manuel/Desktop/bowtie_strategy/SRR6750059_1_1mio.fastq"
out_dir="/Users/manuel/Desktop/bowtie_strategy"
out_filename_bcs="selected_barcodes"
out_filename_umis="selected_umis"
out_filename_gen="selected_gens"


#mprof run --include-children $scripts/select_bcs_umis_genes.py
python3 $scripts/select_bcs_umis_genes.py \
     --sam_in $path_to_cbcs_sam \
     --cbc_comb $path_to_bc_comb \
     --umi_in $path_to_umis_fastq \
     --gen_reads $path_to_gen_fastq \
     --out_dir $out_dir \
     --cbc_out_name $out_filename_bcs \
     --umi_out_name $out_filename_umis \
     --gene_out_name $out_filename_gen
     
#mprof plot
