import pysam
from tools.file_input_output import read_from_file
from tools.utils import get_cmd_args


def add_bc_umi_to_sam(path_to_bc, path_to_umi, sam_in_path, sam_out_path, file_name):
    sam_out_path += "/" + file_name
    bc_list = read_from_file(file_type="txt", input_file=path_to_bc)
    umi_list = read_from_file(file_type="txt", input_file=path_to_umi)
    sam_in = pysam.AlignmentFile(sam_in_path, "r")
    sam_out = pysam.AlignmentFile(sam_out_path, "w", template=sam_in)

    i = 0
    for aligned_read in sam_in.fetch():
        aligned_read.set_tag("BC", bc_list[i])
        aligned_read.set_tag("UI", umi_list[i])
        sam_out.write(aligned_read)
        i += 1


def main(cmd_args):
    file_name = cmd_args['file_name']
    sam_out_path = cmd_args['sam_out']
    sam_in_path = cmd_args['sam_in']
    path_to_umi = cmd_args['umi_in']
    path_to_bc = cmd_args['bc_in']
    add_bc_umi_to_sam(path_to_bc, path_to_umi, sam_in_path, sam_out_path, file_name)


if __name__ == "__main__":
    main(get_cmd_args())