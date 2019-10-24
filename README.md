# SPLiT-seq DGE matrix generation
**work in progress**

## Why this repo?
This repository provides tools to integrate raw scRNA-seq data (fastq files) that have been generated by a SPLiT-seq experiment. The two pipelines being developed will allow the calculation of a digital gene expression (DGE) matrix from raw SPLiT-seq data. Only the .fastq files (paired-end sequencing) and few other files (metadata) are necessary to obtain a DGE matrix. The two pipelines being developed utilize the packages STAR, Drop-seq tools and picard-tools to complement the workflow that is inmplemented with python.
## The SPLiT-seq experiment
The scRNA-seq technology SPLiT-seq was originally published by Rosenberg et al. (["Single-cell profiling of the developing mouse brain and spinal cord with split-pool barcoding"](https://science.sciencemag.org/content/360/6385/176)) in 2018.


RNA transcripts of cells are labeled with cell specific barcodes (cellular barcodes = CBCs) and a uniquq molecular identifier (UMI). The CBCs make it possible to assign RNA transcripts to cells, whereas the UMI allows to distinugish technical from biological replicates.
## Workflow
```
- create file containing barcodes used in SPLiT-seq experiment
- create all possible combinations of barcodes (BCs)
- filter mate reads
  - align BC reads to BC combinations
  - select BC reads with ED < 2 in BC region and UMIs with Phred32 > 10
  - select the corresponding mate reads in Genomic reads .fastq file
  - write selected BC reads, UMIs and genomics reads to .fastq files (BC_filtered.fastq and Genomic_filtered.fastq)
  ```
