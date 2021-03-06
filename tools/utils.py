import getopt
import time
import argparse
import os
import psutil


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


def calculate_memory_usage(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        process = psutil.Process(os.getpid())
        print("The memory usage was: " + str(process.memory_info().rss / 1000000000) + " GB")  # in bytes
        return result
    return wrapper


def get_resources_used(func):
    def wrapper(*args, **kwargs):

        # get the runtime
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        difference = end-start

        hours = int(difference/60)
        minutes = int((difference-(hours*60))/60)
        seconds = int((difference-(minutes*60))/60)
        milliseconds = int((difference-(seconds*60))*1000)

        # get the memory usage
        process = psutil.Process(os.getpid())

        out_put_dir = kwargs['out_dir']
        output_file_name = 'runtime_analyses'

        handler = open(out_put_dir + "/" + output_file_name + ".txt", "w")
        handler.write("The runtime was: " + str(difference) + " seconds")
        handler.write("The runtime was: " + str(hours) + " hrs - " + str(minutes) + " minutes - " + str(seconds) + " seconds - " + str(milliseconds) + " milliseconds")
        handler.write("\n")
        handler.write("The memory usage was: " + str(process.memory_info().rss / 1000000000) + " GB")
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
    parser.add_argument('--mode')
    parser.add_argument('--bc1')
    parser.add_argument('--bc2')
    parser.add_argument('--bc3')
    parser.add_argument('--umi_in')
    parser.add_argument('--bc_in')
    parser.add_argument('--sam_in')
    parser.add_argument('--sam_out')
    parser.add_argument('--cbc_clusters')
    parser.add_argument('--umi_clusters')
    parser.add_argument('--gene_names')
    parser.add_argument('--clusters')
    parser.add_argument('--umi_out_name')
    parser.add_argument('--cbc_out_name')
    parser.add_argument('--gene_out_name')
    parser.add_argument('--accepted_gf')
    parser.add_argument('--cbc_comb')
    parser.add_argument('--file_type')
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