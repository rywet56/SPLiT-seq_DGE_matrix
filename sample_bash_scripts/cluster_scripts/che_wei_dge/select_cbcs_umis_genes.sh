#!/usr/bin/env bash

#$ -l h_rt=20:00:00 -l h_vmem=800G -l h_stack=128M
#$ -o /fast/AG_Ohler/manuel/splitseq/output_file.txt
#$ -V
#$ -e /fast/AG_Ohler/manuel/splitseq/err_file.txt
#$ -pe smp 1
#$ -m ea

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

path_to_cbcs_sam="/fast/AG_Ohler/manuel/che_wei_data/data_2/align_cbcs_ordered.sam"
path_to_bc_comb="/fast/AG_Ohler/manuel/che_wei_data/10X_bc_combinations.fasta"
path_to_umis_fastq="/fast/AG_Ohler/manuel/che_wei_data/data_2/extracted_umis.fastq"
path_to_gen_fastq="/fast/AG_Ohler/manuel/che_wei_data/data_2/gen_reads.fastq"
out_dir="/fast/AG_Ohler/manuel/che_wei_data/data_2"
out_filename_bcs="selected_barcodes"
out_filename_umis="selected_umis"
out_filename_gen="selected_gens"

python3 $scripts/select_bcs_umis_genes.py \
     --sam_in $path_to_cbcs_sam \
     --cbc_comb $path_to_bc_comb \
     --umi_in $path_to_umis_fastq \
     --gen_reads $path_to_gen_fastq \
     --out_dir $out_dir \
     --cbc_out_name $out_filename_bcs \
     --umi_out_name $out_filename_umis \
     --gene_out_name $out_filename_gen
     
