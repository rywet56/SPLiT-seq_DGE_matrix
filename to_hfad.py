import anndata
import scanpy as sc
import numpy as np
from tools.utils import get_cmd_args


def txt_to_hfad(dge_in, dge_out):
    k = sc.read_text(dge_in)

    n_obs = len(k.var)
    n_var = len(k.obs)
    k_t = anndata.AnnData(X=None, shape=(n_obs, n_var))

    k_t.X = k.X.transpose()

    k_t.obs = k.var
    k_t.var = k.obs

    k_t.write(dge_out, compression='gzip')


# txt_to_hfad("/Users/manuel/Desktop/test.txt", "/Users/manuel/Desktop/dge.h5ad")
def convert_to_hfad(dge_in, dge_out, file_type):
    if file_type == ".txt":
        txt_to_hfad(dge_in=dge_in, dge_out=dge_out)


def main(cmd_args):
    input = cmd_args["in_dir"]
    output = cmd_args["out_dir"]
    file_type = cmd_args["file_type"]

    convert_to_hfad(dge_in=input, dge_out=output, file_type=file_type)


if __name__ == "__main__":
    main(get_cmd_args())