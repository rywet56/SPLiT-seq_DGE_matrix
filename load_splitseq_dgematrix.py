import scipy.io as sio


# data_150000_CNS = sio.loadmat('/Users/manuel/Downloads/GSM3017261_150000_CNS_nuclei.mat')
# data_150000_CNS = sio.loadmat('/Users/manuel/Downloads/GSM3017260_100_CNS_nuclei.mat')
# data_150000_CNS = sio.loadmat('/Users/manuel/Downloads/GSM3017263_same_day_cells_nuclei_300_UBCs.mat')
data_150000_CNS = sio.loadmat('/Users/manuel/Downloads/GSM3017265_frozen_preserved_cells_nuclei_200_UBCs.mat')


genes_150000 = data_150000_CNS["genes"]
cells_150000 = data_150000_CNS["barcodes"]
DGE_150000 = data_150000_CNS["DGE"]

print(len(data_150000_CNS["barcodes"]))
print(len(data_150000_CNS["sample_type"]))
print(len(data_150000_CNS["genes"]))

print(str(data_150000_CNS))
# print(data_150000_CNS.keys())
# dict_keys(['__header__', '__version__', '__globals__', 'barcodes', 'genes', 'sample_type', 'DGE'])
handler = open("/Users/manuel/Desktop/DGE_matrix_test.txt", "w")
handler.write("\t")


for column in range(0, len(cells_150000)):
# for column in range(0, 5):
    handler.write(str(cells_150000[column]))
    handler.write("\t")
handler.write("\n")

for row in range(0, len(genes_150000)):
# for row in range(0, 3):
    handler.write(str(genes_150000[row]))
    handler.write("\t")
    # for column in range(0, 5):
    for column in range(0, len(cells_150000)):
        handler.write(str(DGE_150000[column, row]))
        handler.write("\t")
    handler.write("\n")
    print(str(row)+ " of 63940")

handler.close()
