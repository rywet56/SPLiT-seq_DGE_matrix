# This script is used to  extract the gene name for every read from a sam file
# and saves it in a txt file in queryname order.
from tools.file_input_output import read_from_file
from tools.sam_tools import bubble_sort, sort_sam_built_in
from tools.utils import get_cmd_args, get_resources_used


@get_resources_used
def write_gene_names_to_file(path_to_sam, accepted_function, out_dir, file_name):
    read_list = read_from_file(file_type="sam", input_file=path_to_sam)

    sorted_sam = sort_sam_built_in(read_list)

    output = out_dir + "/" + file_name
    handler = open(output + ".txt", "w")


# some gn tags have two genes. intronic mappings can be ignored
    total = 0
    no_mapping = 0
    accepted_genes = 0
    accepted_functions = accepted_function.split(",")

    for entry in sorted_sam:
        total += 1
        if entry.has_tag('gn'):  # did this read align anywhere in the genome?
            gene_names = entry.get_tag('gn').split(',')  # get values for 'gn' tag of this read
            gene_function = entry.get_tag('gf').split(',')  # get values for 'gf' tag of this read
            # accepted_functions = ["CODING", "UTR"]
            intersection = set(gene_function).intersection(accepted_functions)
            # if len(gene_names) < 2:  # test length of value for 'gn' tag for this read
            #     unique_mappings += 1
            #     handler.write(entry.get_tag('gn'))
            if len(intersection) != 0 and len(gene_names) < 2:
                handler.write(entry.get_tag('gn'))
                accepted_genes += 1
            else:
                handler.write('no_gene')
        else:
            no_mapping += 1
            handler.write('no_gene')

        handler.write("\n")

    handler.close()
    print("accepted mappings: " + str(accepted_genes))
    print("number of reads: " + str(total))


def main(cmd_args):
    path_to_sam = cmd_args['sam_in']
    outdir = cmd_args['out_dir']
    filename = cmd_args['file_name']
    accepted_functions = cmd_args['accepted_gf']

    write_gene_names_to_file(path_to_sam=path_to_sam, accepted_function=accepted_functions, out_dir=outdir, file_name=filename)


if __name__ == "__main__":
    main(get_cmd_args())
