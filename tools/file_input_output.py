from Bio import SeqIO


# def file_to_list(path_to_file):
#     # print(path_to_file)
#     handler = open(path_to_file)
#     return handler.readlines()
#
# def fasta_to_list(path_to_file):
#     return remove_fasta_header(remove_newlinetag(file_to_list(path_to_file)))
#
# def txt_to_list(path_to_file):
#     return remove_newlinetag(file_to_list(path_to_file))
#
# def fastq_read_to_list(fastq_file):
#     read_list = []
#
#     for record in SeqIO.parse(fastq_file, "fastq"):
#         read_list.append(str(record.seq))
#
#     return read_list


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


def write_to_file(*args, **kwargs):
    return


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

    handler = open(input_file)

    # importing txt file
    if kwargs["file_type"] == "txt":
        input_list = remove_newlinetag(handler.readlines())
    # importing fasta file
    elif kwargs["file_type"] == "fasta":
        input_list = remove_fasta_header(remove_newlinetag(handler.readlines()))
    # importing fastq file
    elif kwargs["file_type"] == "fastq":
        from Bio import SeqIO

        if kwargs["fastq_reads"]:
            for record in SeqIO.parse(input_file, "fastq"):
                input_list.append(str(record.seq))

        # if kwargs["fastq_complete"]:
        #     import complete fastq in form of a dictionary

    return input_list
