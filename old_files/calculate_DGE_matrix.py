from tools.file_input_output import read_from_file
from tools.utils import get_resources_used
from trials import cluster
from trials.cluster import Cluster


def read_in_clusters(input):
    '''

    '''
    reads = read_from_file(input_file=input, file_type="txt")

    return [e.split("\t") for e in reads]


def make_clusters(reads):
    no_clusters = get_number_of_clusters(reads)
    clusters = []
    for i in range(no_clusters):
        clusters.append(Cluster())

    for read in reads:
        # print(clusters[int(read[1])])
        clusters[int(read[1])-1].add_read(bc_seq=read[0], cluser_size=int(read[2]), umi_no=int(read[3]), gene_name=read[4])

    return clusters


def get_barcode_list(clusters):
    barcodes_no = len(clusters)
    barcodes = [None] * barcodes_no
    for cluster_no in range(barcodes_no):
        barcodes[cluster_no] = clusters[cluster_no].cellular_barcode

    return barcodes


def get_number_of_clusters(reads):
    cluster_no = 0
    for read in reads:
        cluster_no = max(int(read[1]), cluster_no)

    return cluster_no


def get_number_of_genes(gene_list):
    return len(gene_list)


def get_gene_list(clusters):
    gene_list  = []
    for cluster in clusters:
        for gene in cluster.gene_counts.items():
            if gene[0] not in gene_list:
                gene_list.append(gene[0])
    return gene_list


def collapse_cluster_umis(clusters):
    for cluster in clusters:
        cluster.collapse_umis()
    return clusters


def calculate_dge_matrix(clusters, gene_list,):
    count_matrix = []
    cluster_no = len(clusters)
    gene_no = get_number_of_genes(gene_list)
    # generate empty count matrix of dimension gene_no x cluster_no
    for row in range(gene_no):
        count_matrix.append([0]*cluster_no)
    # populate count matrix
    for cluster in range(cluster_no):
        for gene in clusters[cluster].gene_counts.items():
            row = gene_list.index(gene[0])
            col = cluster
            count_matrix[row-1][col-1] = gene[1][0]

    return count_matrix


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
    reads = read_in_clusters(reads_path)
    clusters = make_clusters(reads)
    clusters_umi_collapsed = collapse_cluster_umis(clusters)
    gene_list = get_gene_list(clusters_umi_collapsed)
    barcode_list = get_barcode_list(clusters_umi_collapsed)
    dge_matrix = calculate_dge_matrix(clusters_umi_collapsed, gene_list)
    save_dge_matrix(dge_matrix, gene_list, barcode_list, out_dir, output_file_name)


reads_path = "/Users/manuel/Desktop/BC_UMI_gen.txt"
out_path = "/Users/manuel/Desktop"
out_file_name = "expresseion"
produce_dge_matrix(reads_path, out_dir=out_path, output_file_name=out_file_name)


# cellular_barcode - bc_cluster_no - cluster_size - umi_cluster_no - gene_name_