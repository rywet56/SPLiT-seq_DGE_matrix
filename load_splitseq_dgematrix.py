import scipy.io as sio
import pandas as pd

#Load Data
# data_100_CNS = sio.loadmat('/Users/manuel/Downloads/GSM3017260_100_CNS_nuclei.mat')

# dict_keys(['__header__', '__version__', '__globals__', 'barcodes', 'genes', 'sample_type', 'DGE'])

# # DGE matrix
# DGE = data['DGE']
# # gene names
# genes = pd.Series(data['genes']).str.strip(' ')
#
# handler = open("/Users/manuel/Desktop/DGE_matrix.txt", "w")
# for row in range(0,17032):
#     handler.write(str(genes[row]))
#     for column in range(0,131):
#         handler.write(str(DGE[column,row]))
#         handler.write("\t")
#     handler.write("\n")
#
# handler.close()

# 156049x26894
# print(data_150000_CNS["DGE"].__len__)
# print(data_150000_CNS.keys())
# dict_keys(['__header__', '__version__', '__globals__', 'DGE', 'genes', 'sample_type',
# 'cluster_assignment', 'spinal_cluster_assignment', 'barcodes'])

data_150000_CNS = sio.loadmat('/Users/manuel/Downloads/GSM3017261_150000_CNS_nuclei.mat')

genes_150000 = data_150000_CNS["genes"]
cells_150000 = data_150000_CNS["sample_type"]
DGE_150000 = data_150000_CNS["DGE"]

# print(DGE_150000[, row]])

handler = open("/Users/manuel/Desktop/DGE_matrix_150000_test.txt", "w")
handler.write("\t")
# for column in range(0, len(cells_150000)-1):
for column in range(0, 5):
    handler.write(str(cells_150000[column]))
    handler.write("\t")
handler.write("\n")
# for row in range(0, len(genes_150000)-1):
for row in range(0, 3):
    handler.write(str(genes_150000[row]))
    handler.write("\t")
    for column in range(0, 5):
        handler.write(str(DGE_150000[column, row]))
        handler.write("\t")
    handler.write("\n")

handler.close()

# len(genes_150000)-1
# len(cells_150000)-1
#
# print(cells_150000[156048])
# 156049
# 26894
