import pysam

from tools.sam_tools import sort_sam
from tools.utils import get_cmd_args


def get_unique_reads(sam_in_path, sam_out_path, file_name):
    # orders the reads in queryname order and only pretains a read if it did not map
    # all, mapped once or the read with the highest hit index = 1(HI tag in sam file)

    sam_out_path += "/" + file_name

    sam_in = pysam.AlignmentFile(sam_in_path, "r")

    sam_out = pysam.AlignmentFile(sam_out_path, "w", template=sam_in)

    # sort input sam file according to quryname order
    sam_list = sort_sam(sam_in)
    print("he")
    i = 0
    total_reads = len(sam_list)
    unique_reads = 0
    for read in sam_list:
        if read[0].has_tag('HI'):
            if read[0].get_tag('HI') <= 1:
                sam_out.write(read[0])
                unique_reads += 1
        else:  # for bowtie aligned reads that do not by default have a HI tag
            sam_out.write(read[0])
        i += 1

    print("total reads: " + str(total_reads))
    print("unique reads: " + str(unique_reads))


def main(cmd_args):
    file_name = cmd_args['file_name']
    sam_out_path = cmd_args['sam_out']
    sam_in_path = cmd_args['sam_in']

    get_unique_reads(sam_in_path=sam_in_path, sam_out_path=sam_out_path, file_name=file_name)


if __name__ == "__main__":
    main(get_cmd_args())