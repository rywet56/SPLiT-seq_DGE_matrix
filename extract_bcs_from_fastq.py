from tools.file_input_output import read_from_file, write_to_fastq
from tools.utils import QSanger_to_Phred33


def get_bcs_from_fastq(path_to_barcode_fastq):
    bc_reads_fastq = read_from_file(input_file=path_to_barcode_fastq, file_type="fastq_all")
    bc_reads_fastq_extracted = []

    for read in bc_reads_fastq:
        read_name = read[0]
        read_seq = read[1][10:18] + read[1][48:56] + read[1][86:94]
        read_quality = QSanger_to_Phred33(read[2][10:18] + read[2][48:56] + read[2][86:94])
        bc_reads_fastq_extracted.append((read_name, read_seq, read_quality))

    return bc_reads_fastq_extracted


path_to_barcode_reads = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcode_reads/test_500.fastq"
output_dir = "/Users/manuel/OneDrive/SPLiT-seq/SPLiT-seq_suite/DGE_matrix_generation/metadata/barcode_reads"


extracted_bcs = get_bcs_from_fastq(path_to_barcode_reads)
write_to_fastq(extracted_bcs, output_dir, "extracted_barcodes_500")
