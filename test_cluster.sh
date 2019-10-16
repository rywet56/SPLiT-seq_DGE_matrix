meta_data="/fast/AG_Ohler/manuel/splitseq/150000_nuclei"
scripts=$(pwd)

bc_ref=$meta_data/barcode_combinations.txt
bc_reads=$meta_data/SRR6750042_2.fastq
gen_reads=$meta_data/SRR6750042_1.fastq
out_dir=$meta_data

python3 $scripts/filter_barcodes_advanced.py \
    --bc_reference $bc_ref \
    --bc_reads $bc_reads \
    --gen_reads $gen_reads \
    --out_dir $out_dir

