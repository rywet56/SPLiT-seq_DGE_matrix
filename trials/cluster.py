class Cluster:
    def __init__(self):
        self.cellular_barcode = ""
        self.umis = None
        self.gene_names = None
        self.cluster_size = 0
        self.gene_counts = {}

    def add_read(self, bc_seq, cluser_size, umi_no, gene_name):
        '''
        :param cluser_size:
        :param bc_seq:
        :param umi_no:
        :param gene_name:
        :param umi: the umi number assigned by starcode, not the umi sequence
        :return:
        '''
        # intitialize Cluster object if Cluster object is empty
        if self.cellular_barcode == "":
            self.cellular_barcode = bc_seq
            self.umis = [None] * cluser_size
            self.gene_names = [None] * cluser_size

        # add information about umi and gene_name of read
        self.umis[self.cluster_size] = umi_no
        self.gene_names[self.cluster_size] = gene_name

        # increase cluster size
        self.cluster_size += 1

        # print("cluster name: " + self.cellular_barcode)
        # print("cluster umis: " + str(self.umis))
        # print("gene names: " + str(self.gene_names))
        # print("cluster size: " + str(self.cluster_size))
        # print("-----------------------------------")

    def collapse_umis(self):
        for i in range(len(self.gene_names)):
            if self.gene_names[i] in self.gene_counts:  # is gene already listed?
                if self.umis[i] not in self.gene_counts[self.gene_names[i]][1]:  # check existence of UMI for this gene
                    self.gene_counts[self.gene_names[i]][1].append(self.umis[i])  # if umi not present add umi number
                    self.gene_counts[self.gene_names[i]][0] += 1  # and increase gene count
            else:  # if gene_name does not exist already, add it to the gene_counts list
                self.gene_counts[self.gene_names[i]] = [1, [self.umis[i]]]





