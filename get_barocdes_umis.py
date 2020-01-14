# This script can be use to extract the barcode or umi from the original oligo

from create_bc_comb import extract_barcodes
from tools.file_input_output import read_from_file, write_to_txt

bc1_path="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper/r1barcodes.txt"
out_put_dir="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper"
bc1_cleaned = read_from_file(input_file=bc1_path, file_type="txt")
bc1_extracted = extract_barcodes(bc1_cleaned)
write_to_txt(bc1_extracted, out_put_dir, "bc1_isolated")

bc2_path="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper/r2barcodes.txt"
out_put_dir="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper"
bc2_cleaned = read_from_file(input_file=bc2_path, file_type="txt")
bc2_extracted = extract_barcodes(bc2_cleaned)
write_to_txt(bc2_extracted, out_put_dir, "bc2_isolated")

bc3_path="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper/r3barcodes.txt"
out_put_dir="/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcodes_paper"
bc3_cleaned = read_from_file(input_file=bc3_path, file_type="txt")
bc3_extracted = extract_barcodes(bc3_cleaned, UMI=True)
write_to_txt(bc3_extracted, out_put_dir, "bc3_isolated")