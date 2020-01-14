#!/usr/bin/env bash

scripts="/fast/AG_Ohler/manuel/splitseq/SPLiT-seq_DGE_matrix"

#k=42
#for ((i=1; i<2; i++))
#do
#    # set paths for input and output
#    bc_reads="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/batch_"$i"/SRR67500"$k"_2.fastq"
#    output="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/extracted_cbcs_umis"
#    umi_out_name="extracted_umis_b"$i
#    cbc_out_name="extracted_cbcs_b"$i
#    k=$(($k+1))
#
#    # start job
#    qsub \
#    -l h_rt=20:00:00 -l h_vmem=370G -l h_stack=128M \
#    -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt \
#    -V \
#    -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt \
#    -pe smp 1 \
#    -m ea
#    python3 $scripts/extract_cbc_umi.py \
#    --bc_reads $bc_reads \
#    --out_dir $output \
#    --cbc_out_name $cbc_out_name \
#    --umi_out_name $umi_out_name
#
#done
    
# set paths for input and output
bc_reads="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/batch_1/SRR6750042_2.fastq"
output="/fast/AG_Ohler/manuel/splitseq/150000_nuclei/extracted_cbcs_umis"
umi_out_name="extracted_umis_b4
cbc_out_name="extracted_cbcs_b4

qsub $((echo $((4+56))))

#qsub \
#    -l h_rt=20:00:00 -l h_vmem=370G -l h_stack=128M \
#    -o /fast/AG_Ohler/manuel/splitseq/output_file_more_stack.txt \
#    -V \
#    -e /fast/AG_Ohler/manuel/splitseq/err_file_more_stack.txt \
#    -pe smp 1 \
#    -m ea \
#    python3 $scripts/extract_cbc_umi.py \
#    --bc_reads $bc_reads \
#    --out_dir $output \
#    --cbc_out_name $cbc_out_name \
#    --umi_out_name $umi_out_name
    




