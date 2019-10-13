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
    parser = argparse.ArgumentParser(prog='PROG', description='filtering bc_reads')
    parser.add_argument('--bc_reference')
    parser.add_argument('--bc_reads')
    parser.add_argument('--gen_reads')
    parser.add_argument('--out_dir', help='output direcotry')
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

