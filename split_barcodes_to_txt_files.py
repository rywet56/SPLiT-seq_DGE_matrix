from Bio import SeqIO

def fastq_seq_to_list(path_to_fastq):
    fastq_sequences = []
    for record in SeqIO.parse(path_to_fastq, "fastq"):
        fastq_sequences.append(str(record.seq))

    return fastq_sequences

# splits barcode reads into 4 separate files
def fastq_barcodes_to_txt(path_to_fastq, output_location, UMI=(1,10),
                            BC1=(87,94), BC2=(49,56), BC3=(11,18)):
    umi = open(output_location + "/UMI.txt", "w")
    bc1 = open(output_location + "/BC1.txt", "w")
    bc2 = open(output_location + "/BC2.txt", "w")
    bc3 = open(output_location + "/BC3.txt", "w")
    barcode_sequence = fastq_seq_to_list(path_to_fastq)
    umi_list=[]

    for read in barcode_sequence:
        umi.write(read[UMI[0]-1:UMI[1]])
        umi.write("\n")

        bc1.write(read[BC1[0]-1:BC1[1]])
        bc1.write("\n")

        bc2.write(read[BC2[0]-1:BC2[1]])
        bc2.write("\n")

        bc3.write(read[BC3[0]-1:BC3[1]])
        bc3.write("\n")

    umi.close()
    bc1.close()
    bc2.close()
    bc3.close()



path_to_barcode_fastq = "/Users/manuel/Desktop/SPLiT-seq mouse brain/mouse_brain_2.fastq"
output_location = "/Users/manuel/Desktop/SPLiT-seq mouse brain"
fastq_barcodes_to_txt(path_to_barcode_fastq, output_location)
