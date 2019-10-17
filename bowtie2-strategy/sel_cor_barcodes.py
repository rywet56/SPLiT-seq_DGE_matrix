import pysam

# reference for methods
# https://buildmedia.readthedocs.org/media/pdf/pysam/latest/pysam.pdf

aligned_sam = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/barcode_correction/barcode_correction_alignment/barcodes_aligned.sam"
samfile = pysam.AlignmentFile(aligned_sam, "r")

aligned = 0
for aligned_read in samfile.fetch():
    # print(aligned_read.get_forward_sequence()) gives you the aligned sequence
    # print(aligned_read.get_tags())
    if aligned_read.get_tags()[0][1] :
        aligned += 1

print(aligned)

# GGAAAAGGAAAAAAAAGGGGGGGG
# CGCTGATCCACTTCGAAGTGGTCA
# CCGACATCAGCAGGAACAAGACTA

