import getopt
import time
import argparse


def calculate_runtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        out_put_dir = kwargs['out_dir']
        output_file_name = 'runtime_analyses'
        handler = open(out_put_dir + "/" + output_file_name + ".txt", "w")
        handler.write("the runtime was: " + str(end-start) + " seconds")
        handler.close()

        return result

    return wrapper


def get_cmd_args():
    """
    accepts a list of cmd arguments and interprets them.
    the input can be any combinateion of possible flags (see the flags added in add_argument)
    :return:
    """
    parser = argparse.ArgumentParser(prog='PROG', description='filtering bc_reads')
    parser.add_argument('--bc_reference')
    parser.add_argument('--bc_reads')
    parser.add_argument('--gen_reads')
    parser.add_argument('--in_dir')
    parser.add_argument('--out_dir', help='output direcotry')
    parser.add_argument('--file_name')
    args = parser.parse_args()
    # args_dic = vars(args)

    return vars(args)


def return_cmd_args(args):
    opts_and_args, args = getopt.getopt(args, "r:b:g:o:", ["bc_reference=", "bc_reads=", "gen_reads=", "out_dir="])

    bc_reference = ''
    bc_reads = ''
    genomic_reads = ''
    out_dir = ''

    for opt, arg in opts_and_args:
        if opt in ("-r", "--bc_reference"):
            bc_reference = arg
        elif opt in ("-b", "--bc_reads"):
            bc_reads = arg
        elif opt in ("-g", "--gen_reads"):
            genomic_reads = arg
        elif opt in ("-o", "--out_dir"):
            out_dir = arg

    return bc_reference, bc_reads, genomic_reads, out_dir


def QSanger_to_Phred33(score_list):
    """
    expects a list of scores in QSanger format and converts to Phred33 score
    :param score_list: a list of scores in QSanger format
    :return: a list of QSanger scores encoded in ASCII
    """
    Phred33_list = []
    for score in score_list:
        Phred33_list.append(chr(round(score) + 33))
    return Phred33_list