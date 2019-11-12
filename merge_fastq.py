from tools.file_input_output import read_from_file, write_to_fastq
from tools.utils import get_cmd_args, calculate_memory_usage, calculate_runtime, get_resources_used


def get_input_locations(s):
    return s.split(';')


@get_resources_used
def merge_fastq(input_directories, out_dir, output_file_name):
    # get input locations of fastq files
    directories_list = get_input_locations(input_directories)
    # initialize list that will be filled with content of fastq files
    fastq_files = [None]*len(directories_list)
    # read in input fastq files
    for i in range(len(fastq_files)):
        fastq_files[i] = read_from_file(input_file=directories_list[i], file_type='fastq_all')

    for fastq in fastq_files:
        write_to_fastq(fastq, out_dir, output_file_name, mode="append")


def main(cmd_args):
    input_fastq_files = cmd_args["in_dir"]
    out_put_dir = cmd_args["out_dir"]
    filename = cmd_args["file_name"]

    merge_fastq(input_directories=input_fastq_files, out_dir=out_put_dir, output_file_name=filename)


if __name__ == "__main__":
    main(get_cmd_args())