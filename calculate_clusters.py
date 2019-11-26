from tools.file_input_output import read_from_file
from tools.utils import get_resources_used, get_cmd_args


def get_gene_name(genes, read_id):
    '''
    the read_id has nothing to do with the query_name in the fastq file
    :param read_id: an integer that specifies the line number of a read
    :return: a gene name as a string
    '''
    return genes[int(read_id)-1]


def get_umi_number(read_umi_list, read_number):
    return read_umi_list[read_number-1]


def get_read_umi_list(umis, number_of_reads):
    '''
    Returns a list that maps umi_cluster number to read_number
    :param umis: a list that contains clustering results of UMI's. Every list entry corresponds to one cluster.
                [ "ACTCTGCTAG\t134\t23,54,84,2,1", ... ]
    :param number_of_reads:
    :return: [umi_cluster_number, ...]  --> The first umi_cluster_number corresponds to the gene of position 1 that has been read in
    '''
    read_umi_list = [0]*number_of_reads
    for cluster_number in range(len(umis)):  # go through all umi clusters
        read_numbers = umis[cluster_number].split("\t")[2].split(",")  # read_numbers = line numbers
        for read_number in read_numbers:
            read_umi_list[int(read_number)-1] = cluster_number+1
    return read_umi_list


def get_number_of_reads(gene_list):
    return len(gene_list)


def get_gene_name_list(gene):
    # return gene[0].split('\n')
    return gene


@get_resources_used
def construct_cluster_umi_file(barcodes, umis, genes, out_dir, file_name):
    '''
    Combines the information of CBC and UMI clustering with gene names from alignment of
    genomic reads into one file that can be used to construct a DGE matrix in another step.
    :param barcodes: [ "ACTCTGCTAG\t134\t23,54,84,2,1", ... ]
    :param umis: [ "ACTCTGCTAG\t134\t23,54,84,2,1", ... ]
    :param genes: [gene_1, gene_2, gene45, ... ]
    '''
    handler = open(out_dir + "/" + file_name + ".txt", "w")

    gene_list = get_gene_name_list(genes)
    no_reads = get_number_of_reads(gene_list)
    read_umi_list = get_read_umi_list(umis, no_reads)

    for cluster in barcodes:
        clust = cluster.split("\t")
        # print(clust)  --> ['GAGCTGAAAAAGGAGCGTCGTAGA', '1', '979855']
        cluster_name = clust[0]
        cluster_size = clust[1]
        handler.write(cluster_name + "\t" + str(cluster_size) + "\t")

        read_numbers = clust[2].split(",")  # line numbers of clustered barcode reads

        no_reads = len(read_numbers)
        for read in range(no_reads):
            read_no = int(read_numbers[read])
            gene_name = get_gene_name(gene_list, read_no)
            umi_number = str(get_umi_number(read_umi_list, read_no))

            if gene_name != "no_gene":  # only write gene name of read and umi_number of that read if it is not no_gene
                handler.write(gene_name + ',' + umi_number)
                if read < no_reads-1:
                    handler.write(",")
            #  if the gene name associated with the read is "no_gene", do not perform any action
            #  just let things empty for that cluster

        handler.write("\n")

    # some check --> to be removed later
    no_genes = 0
    no_no_gene = 0
    for gen in genes:
        if gen != "no_gene":
            no_genes += 1
        else:
            no_no_gene += 1

    print("number of clusters: " + str(len(barcodes)))
    print("number of reads: " + str(len(genes)))
    print("number of accepted reads: " + str(no_genes))
    print("number of no_genes: " + str(no_no_gene))


def main(cmd_args):
    path_to_barcodes = cmd_args['cbc_clusters']
    barcodes = read_from_file(input_file=path_to_barcodes, file_type="txt")

    path_to_umis = cmd_args['umi_clusters']
    umis = read_from_file(input_file=path_to_umis, file_type="txt")

    path_to_genes = cmd_args['gene_names']
    genes = read_from_file(input_file=path_to_genes, file_type="txt")

    # gene_no = 0
    # for gen in genes:
    #     if gen != "no_gene":
    #         gene_no += 1
    # print(gene_no)

    output_file_name = cmd_args["file_name"]
    out_put_dir = cmd_args["out_dir"]

    construct_cluster_umi_file(barcodes, umis, genes, out_dir=out_put_dir, file_name=output_file_name)


if __name__ == "__main__":
    main(get_cmd_args())
