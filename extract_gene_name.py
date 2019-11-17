# This script is used to  extract the gene name for every read from a sam file
# and saves it in a txt file in queryname order.
from tools.file_input_output import read_from_file
from tools.sam_tools import bubble_sort

path_to_sam = "/Users/manuel/Desktop/genfun_tagged.sam"
output_dir = "/Users/manuel/Desktop"
output_filename = "sorted.txt"
output = output_dir + "/" + output_filename
read_list = read_from_file(file_type="sam", input_file=path_to_sam)

sorted_sam = bubble_sort(read_list)

handler = open(output, "w")

for entry in sorted_sam:
    if entry[0].has_tag('gn'):
        handler.write(entry[0].get_tag('gn'))
    else:
       handler.write('no_gene')
    handler.write("\n")

handler.close()
