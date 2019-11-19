from tools.file_input_output import read_from_file
from tools.utils import get_resources_used, get_cmd_args
from cluster import Cluster


def read_in_clusters(path_to_cluster_file):
    '''

    '''
    clusters_raw = read_from_file(input_file=path_to_cluster_file, file_type="txt")
    no_clusters = get_number_of_clusters(clusters_raw)
    clusters = []
    for cluster_no in range(no_clusters):
        clusters.append(Cluster())

    print("empty clusters formed")
    for cluster_no in range(no_clusters):
        cluster = clusters_raw[cluster_no].split('\t')
        clusters[cluster_no].add_reads(bc_seq=cluster[0], cluster_size=cluster[1], gene_umi_list=cluster[2])

    print("clusters populated")
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


def get_number_of_genes(gene_list):
    return len(gene_list)


def collapse_cluster_umis(clusters):
    for cluster in clusters:
        # print(cluster)
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
    print("DGE matrix contains: " + str(cluster_no) + " cells")

    handler = open("/Users/manuel/Desktop/some_statistics", "w")
    handler.write("barcodes\tnumber of genes\n")
    for cluster in clusters:
        handler.write(cluster.cellular_barcode + "\t" + str(len(cluster.gene_counts)) + "\n")

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
    clusters = read_in_clusters(reads_path)
    # clusters = make_clusters(reads)
    clusters_umi_collapsed = collapse_cluster_umis(clusters)
    print("umis collapsed")
    gene_list = get_gene_list(clusters_umi_collapsed)
    print("gene list obtained")
    barcode_list = get_barcode_list(clusters_umi_collapsed)
    print("barcode list obtained")
    dge_matrix = calculate_dge_matrix(clusters_umi_collapsed, gene_list)
    print("matrix calculated")
    save_dge_matrix(dge_matrix, gene_list, barcode_list, out_dir, output_file_name)


def main(cmd_args):
    path_to_clusters = cmd_args['clusters']
    out_put_dir = cmd_args["out_dir"]
    out_file_name = cmd_args["file_name"]

    produce_dge_matrix(path_to_clusters, out_dir=out_put_dir, output_file_name=out_file_name)
    print("done!!!")


if __name__ == "__main__":
    main(get_cmd_args())