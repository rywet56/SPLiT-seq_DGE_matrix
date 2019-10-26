# SPLiT-seq DGE matrix generation
**work in progress**

## Why this repo?
This repository provides tools to integrate raw scRNA-seq data (fastq files) that have been generated by a SPLiT-seq experiment. The two pipelines being developed will allow the calculation of a digital gene expression (DGE) matrix from raw SPLiT-seq data. Only the .fastq files (paired-end sequencing) and few other files (metadata) are necessary to obtain a DGE matrix. The two pipelines being developed utilize the aligners [STAR](https://github.com/alexdobin/STAR) and [Bowtie2](https://github.com/alexdobin/STAR), and functions from [Drop-seq tools](https://github.com/broadinstitute/Drop-seq/releases) and [picard-tools](https://broadinstitute.github.io/picard/). All other functionalities are implemented in python and can be executed in bash scripts with parameters specifying input (.fastq files, reference genome, etc.) and other options (alignment depth, output file names etc.).
## BACKGROUND: The SPLiT-seq experiment
The scRNA-seq technology SPLiT-seq was originally published by Rosenberg et al. (["Single-cell profiling of the developing mouse brain and spinal cord with split-pool barcoding"](https://science.sciencemag.org/content/360/6385/176)) in 2018.
### Split-Barcode-Pool
Cells or nuclei of any tissue type are split into wells (96 well plate) containing different barcodes. Those well-specific barcodes are ligated to the 3' end of (ideally) all RNA transcripts in every cell within every well. After this barcoding step, cells are pooled and split again into wells containig different barcodes which are added to all RNA transcripts. Cells from all wells are pooled again. This sequence of splitting, barcoding and pooling is performed three times in the original protocol. It could be performed more often to create more possible barcode combinations.
 <p align="center">
 <img src="https://user-images.githubusercontent.com/43107602/67619243-68e0ef80-f7f9-11e9-9bf1-0302d60971c6.png" width="400">
 </p>

### The barcode structure
After barcoding, a template switch is introduced, cells are lysed and the barcoded transcripts are aplified via PCR to generate a sequencing library. The barcoded transcript now contains sequencing adapters on both ends.
The three barcodes (pink, green and blue) make up the cell-specific barcode. All transcripts from the same cell are suposed to have the same barcode combination (the same cellular barcode). The brownish sequence corresponds to the UMI and allows to distinugish technical from biological replicates.

In that way, the cellular barcode (CBC) allows to group transcripts (expressed genes) to cells and the UMI allows to determine the number of biological copies of every transcript (UMI count per unique transcript).

Sequencing then produces two reads per barcoded transcipt that are stored in genomics_read.fastq and barcode_reads.fastq. Those files are used in the processing of raw reads in the pipeline developed (as described below)
 <p align="center">
  <img src="https://user-images.githubusercontent.com/43107602/67618927-bf4c2f00-f7f5-11e9-8724-719dcf57a3c4.png"  width="500">
 </p>

## PIPELINE: Sequencing read analysis
- create file containing barcodes used in SPLiT-seq experiment
- create all possible combinations of barcodes (BCs)
- filter mate reads
  - align BC reads to BC combinations
  - select BC reads with ED < 2 in BC region and UMIs with Phred32 > 10
  - select the corresponding mate reads in Genomic reads .fastq file
  - write selected BC reads, UMIs and genomics reads to .fastq files (BC_filtered.fastq and Genomic_filtered.fastq)
 
 <p align="center">
  <img src="https://user-images.githubusercontent.com/43107602/67587832-ec94d080-f754-11e9-93e2-1229cabe570b.png"  width="373">
 </p>

