from tools.file_input_output import read_from_file
from tools.utils import get_resources_used, get_cmd_args
from cluster import Cluster


def read_in_clusters(path_to_cluster_file):
    clusters_raw = read_from_file(input_file=path_to_cluster_file, file_type="txt")
    no_clusters = get_number_of_clusters(clusters_raw)
    clusters = []
    print("number of clusters: " + str(no_clusters))
    for cluster_no in range(no_clusters):
        clusters.append(Cluster())
    print("empty clusters formed")

    for cluster_no in range(no_clusters):
        cluster = clusters_raw[cluster_no].split('\t')
        # print(cluster)
        if len(cluster) == 3:
            clusters[cluster_no].add_reads(bc_seq=cluster[0], cluster_size=cluster[1], gene_umi_list=cluster[2])
        else:
            clusters[cluster_no].add_reads(bc_seq=cluster[0], cluster_size=0, gene_umi_list="")
    print("clusters populated")

    # # to be removed
    # total = 0
    # accepted_reads = 0
    # no_no_genes = 0
    # for cluster in clusters:
    #     total += len(cluster.umis)
    #     for read in cluster.gene_names:
    #         if read != "no_gene":
    #             accepted_reads += 1
    #         else:
    #             no_no_genes += 1
    #
    # print("number of accepted reads: " + str(accepted_reads))
    # print("total reads: " + str(total))
    # print("number of no_genes: " + str(no_no_genes))

    return clusters


def get_barcode_list(clusters):
    barcodes_no = len(clusters)
    barcodes = [None] * barcodes_no
    for cluster_no in range(barcodes_no):
        barcodes[cluster_no] = clusters[cluster_no].cellular_barcode

    return barcodes


def get_number_of_clusters(cluster_list):
    return len(cluster_list)


def get_gene_list(clusters):
    gene_list  = []
    for cluster in clusters:
        for gene in cluster.gene_counts.items():
            if gene[0] not in gene_list:
                gene_list.append(gene[0])
    return gene_list


def get_unique_genes(gene_list):
    '''
    Returns the numbner of unique genes in gene_list.
    :param gene_list:
    :return:
    '''
    unique_genes_list = []
    for gene in gene_list:
        if gene not in unique_genes_list:
            unique_genes_list.append(gene)
    return unique_genes_list, len(unique_genes_list)


def collapse_cluster_umis(clusters):
    counts_per_cluster = [None]*len(clusters)
    umis_per_cluster = [None]*len(clusters)
    i = 0
    for cluster in clusters:
        # collapse umis
        cluster.collapse_umis()  # --> clusters that have no genes will have an empty gene_counts dic

        # get count information
        gene_counts = 0
        for counts in cluster.gene_counts.values():
            # print(counts[0])
            gene_counts += counts[0]
        counts_per_cluster[i] = gene_counts
        umis_per_cluster[i] = cluster.cluster_size
        i += 1
    return clusters, counts_per_cluster, umis_per_cluster


def calculate_dge_matrix(clusters, gene_list, counts_per_cluster, umis_per_cluster, out_dir):
    count_matrix = []
    cluster_no = len(clusters)
    unique_genes, gene_no = get_unique_genes(gene_list)  # gets unique genes and number of unique genes

    # generate empty count matrix of dimension gene_no x cluster_no
    for row in range(gene_no):
        count_matrix.append([0]*cluster_no)

    # populate count matrix
    for cluster in range(cluster_no):
        for gene in clusters[cluster].gene_counts.items():  # interates through contents of gene_count list
            row = unique_genes.index(gene[0])  # gets the position of the gene gene[0] in gene_list
            col = cluster
            count_matrix[row][col] = gene[1][0]  # gets the number of transcripts for that gene

    save_statistics(out_dir, clusters, counts_per_cluster, umis_per_cluster)

    return count_matrix, unique_genes


def save_statistics(out_dir, cluster_list, counts_per_cluster, umis_per_cluster):
    handler = open(out_dir + "/cluster_statistics.txt", "w")

    handler.write("barcodes\tgenes\tcounts\tumis\n")

    for clus_number in range(len(cluster_list)):
        handler.write(cluster_list[clus_number].cellular_barcode + "\t" + str(len(cluster_list[clus_number].gene_counts)) + "\t")
        handler.write(str(counts_per_cluster[clus_number]) + "\t")
        handler.write(str(umis_per_cluster[clus_number]) + "\n")


def save_dge_matrix(dge_matrix, gene_list, barcode_list, output_directory, output_file_name):
    handler = open(output_directory + "/" + output_file_name + ".txt", "w")

    for barcode in barcode_list:
        handler.write("\t")
        handler.write(barcode)

    handler.write("\n")

    for gene in range(len(gene_list)):
        handler.write(gene_list[gene])
        for count in dge_matrix[gene]:
            handler.write("\t")
            handler.write(str(count))
        handler.write("\n")


@get_resources_used
def produce_dge_matrix(reads_path, out_dir, output_file_name):
    clusters = read_in_clusters(reads_path)
    # clusters = make_clusters(reads)
    clusters_umi_collapsed, counts_per_cluster, umis_per_cluster = collapse_cluster_umis(clusters)
    # counts = 0
    # for count in counts_per_cluster:
    #     counts += int(count)
    # print(counts)
    print("umis collapsed")
    gene_list = get_gene_list(clusters_umi_collapsed)
    print("gene list obtained")
    barcode_list = get_barcode_list(clusters_umi_collapsed)
    print("barcode list obtained")
    dge_matrix, unique_genes = calculate_dge_matrix(clusters_umi_collapsed, gene_list, counts_per_cluster, umis_per_cluster, out_dir)
    print("matrix calculated")
    save_dge_matrix(dge_matrix, unique_genes, barcode_list, out_dir, output_file_name)
    print("DGE matrix written to file")


def main(cmd_args):
    path_to_clusters = cmd_args['clusters']
    out_put_dir = cmd_args["out_dir"]
    out_file_name = cmd_args["file_name"]

    produce_dge_matrix(path_to_clusters, out_dir=out_put_dir, output_file_name=out_file_name)


if __name__ == "__main__":
    main(get_cmd_args())