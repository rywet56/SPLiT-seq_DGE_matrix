import pysam
from tools.file_input_output import read_from_file
from tools.utils import get_cmd_args
from tools.sam_tools import sort_sam


def same_length(sam_in_path):
    sam_in = pysam.AlignmentFile(sam_in_path, "r")
    length = 0
    for read in sam_in.fetch():
        if read:
            length += 1

    return length


def same_dimension(path_to_bc, path_to_umi, sam_in_path):
    bc_list = read_from_file(file_type="txt", input_file=path_to_bc)
    umi_list = read_from_file(file_type="txt", input_file=path_to_umi)


def add_bc_umi_to_sam(path_to_bc, path_to_umi, sam_in_path, sam_out_path, file_name, cbc_range, umi_range,
                      umi_cbc_file_type="txt"):
    sam_in = pysam.AlignmentFile(sam_in_path, "r")
    # tes if dimensions of input are correct

    # sort input sam file according to quryname order
    sam_list = sort_sam(sam_in)

    sam_out_path += "/" + file_name
    bc_list = read_from_file(file_type=umi_cbc_file_type, input_file=path_to_bc)
    umi_list = read_from_file(file_type=umi_cbc_file_type, input_file=path_to_umi)
    sam_out = pysam.AlignmentFile(sam_out_path, "w", template=sam_in)

    i = 0
    for read in sam_list:
        read[0].set_tag("XC", bc_list[i][cbc_range[0]-1:cbc_range[1]])
        read[0].set_tag("XM", umi_list[i][umi_range[0]-1:umi_range[1]])
        sam_out.write(read[0])
        i += 1


def main(cmd_args):
    file_name = cmd_args['file_name']
    sam_out_path = cmd_args['sam_out']
    sam_in_path = cmd_args['sam_in']
    path_to_umi = cmd_args['umi_in']
    path_to_bc = cmd_args['bc_in']
    add_bc_umi_to_sam(path_to_bc, path_to_umi, sam_in_path, sam_out_path, file_name, cbc_range=[9,24], umi_range=[0,10])


if __name__ == "__main__":
    main(get_cmd_args())