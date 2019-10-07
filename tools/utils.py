import getopt
import time


def calculate_runtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        out_put_dir = args[2]
        output_file_name = 'runtime_analyses'
        handler = open(out_put_dir + "/" + output_file_name + ".txt", "w")
        handler.write("the runtime was: " + str(end-start) + " seconds")
        handler.close()

        return result

    return wrapper


def return_cmd_args(args):
    opts_and_args, args = getopt.getopt(args, "r:b:o:", ["bc_reference=", "bc_reads=", "out_dir="])

    bc_reference = ''
    bc_reads = ''
    out_dir = ''

    for opt, arg in opts_and_args:
        if opt in ("-r", "--bc_reference"):
            bc_reference = arg
        elif opt in ("-b", "--bc_reads"):
            bc_reads = arg
        elif opt in ("-o", "--out_dir"):
            out_dir = arg

    return bc_reference, bc_reads, out_dir

