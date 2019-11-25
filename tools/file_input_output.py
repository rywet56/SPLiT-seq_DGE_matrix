import pysam

from tools.utils import QSanger_to_Phred33


def remove_newlinetag(some_list):
    some_list_newlineremoved = []
    for entry in some_list:
        some_list_newlineremoved.append(entry.rstrip())

    return some_list_newlineremoved


def remove_fasta_header(some_list):
    return some_list[1:]


def extract_barcodes_to_txt(fastq_file, output_directory, output_file_name):
    fastq_read_list = fastq_read_to_list(fastq_file)
    handler = open(output_directory + "/" + output_file_name + ".txt", "w")
    for read in fastq_read_list:
        handler.write(read[86:94] + read[48:56] + read[10:18])
        handler.write("\n")

    handler.close()


def write_to_txt(input_list, output_directory, output_file_name):
    handler = open(output_directory + "/" + output_file_name + ".txt", "w")

    for read in input_list:
        handler.write(read + "\n")
    handler.close()


def write_to_fastq(fastq_list, output_directory, output_file_name, mode="write"):
    if mode == "write":
        handler = open(output_directory + "/" + output_file_name + ".fastq", "w")
    elif mode == "append":
        handler = open(output_directory + "/" + output_file_name + ".fastq", "a")

    for read in fastq_list:
        # print(read[0])
        handler.write("@" + read[0] + "\n")
        handler.write(read[1] + "\n")
        handler.write("+\n")
        phred33_list = QSanger_to_Phred33(read[2])
        handler.write(''.join(str(e) for e in phred33_list) + "\n")
    handler.close()


def read_from_file(*args, **kwargs):
    """
    This function can be used to read content of fastq, fasta and txt files into a list. This list is returned
    by this function
    :param args: this option is not used yet
    :param kwargs: possible keyword arguments are:
    input_file --> the full path to the file that should be imported including the full file name
    input_dir --> the full path to the file that should be imported
    input_filename --> the full file name of the file that should be imported
    file_type --> the type of the file that should be imported
    fastq_reads --> an option specifying that only reads should be implemented from the fastq file

    :return:
    """
    input_dir = ''
    input_filename = ''
    input_file = ''
    input_list = []
    input_dic = {}

    if kwargs["input_file"]:  # check if input_file has been supplied to the function
        input_file = kwargs["input_file"]
    else:  # if no input file name has been supplied, look for the input directory and file name and concatenate
        input_dir = kwargs["input_dir"]
        input_filename = kwargs["input_filename"]
        input_file = input_dir + "/" + input_filename

    try:
        handler = open(input_file)
    except FileNotFoundError as exception:
        print("file was not found!!")
        print(exception)
    else:
        # importing txt file
        if kwargs["file_type"] == "txt":
            input_list = remove_newlinetag(handler.readlines())
        # importing fasta file
        elif kwargs["file_type"] == "fasta":
            input_list = remove_fasta_header(remove_newlinetag(handler.readlines()))
        # importing fastq file
        elif kwargs["file_type"] == "fastq_all":
            from Bio import SeqIO

            for record in SeqIO.parse(input_file, "fastq"):
                read_name = str(record.description)
                read_seq = str(record.seq)
                read_qual = record.letter_annotations["phred_quality"]
                input_list.append((read_name, read_seq, read_qual))

        elif kwargs["file_type"] == "sam":
            """
            structure of returned sam list:
            [ [AlignmentFile_object, query_name_number], [], ... ]
            """
            sam = pysam.AlignmentFile(input_file, "r")
            input_list = []
            for query in sam.fetch():
                # query_no = query.query_name.split(".")[1]
                input_list.append([query, query.query_name])

    return input_list
