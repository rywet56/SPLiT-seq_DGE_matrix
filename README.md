# SPLiT-seq DGE matrix generation

## Why this repo?
The ability to describe gene expression levels at the level of single cells is becoming more and more important. That is because it allows us to describe the heterogenety of cells on the level of transcriptomes. This detailed description of differences among cells (of the same or different cell type) is crucial to better understand how different cell types and functions are defined. The knowledge gained through scRNA-seq experiments will help us to understand the development of disease in more detail and hopefully enable us to re-enigneer cells functioning "out of order" and thereby heal disease.

One very elegant way to perform scRNA-seq is by using "split-pool ligation-based transcriptome sequencing" (SPLiT-seq), first published by Rosenberg et al. (["Single-cell profiling of the developing mouse brain and spinal cord with split-pool barcoding"](https://science.sciencemag.org/content/360/6385/176)) in 2018.

This repository provides tools to integrate raw scRNA-seq data (fastq files) that have been generated by a SPLiT-seq experiment. The two pipelines being developed will allow the calculation of a digital gene expression (DGE) matrix from raw SPLiT-seq data. Only the .fastq files (paired-end sequencing) and few other files (metadata) are necessary to obtain a DGE matrix. The two pipelines being developed utilize the aligners [STAR](https://github.com/alexdobin/STAR) and [Bowtie2](https://github.com/alexdobin/STAR), and functions from [Drop-seq tools](https://github.com/broadinstitute/Drop-seq/releases) and [picard-tools](https://broadinstitute.github.io/picard/). All other functionalities are implemented in python and can be executed in bash scripts with parameters specifying input (.fastq files, reference genome, etc.) and other options (alignment depth, output file names etc.).
## BACKGROUND: The SPLiT-seq experiment
### Split-Barcode-Pool
Extracted cells or nuclei of any tissue type are split into wells (96 well plate) containing different barcodes. Those well-specific barcodes are ligated to the 3' end of (ideally) all RNA transcripts in every cell within every well. After this barcoding step, cells are pooled and split again into wells containig different barcodes which are added to all RNA transcripts. Cells from all wells are pooled again. This sequence of splitting, barcoding and pooling is performed three times in the original protocol. In every step step, a barcode is attached to the RNA transcripts within in each cell. More rounds of barcoding could be performed to create more possible barcode combinations and therefore allow to sequence more cells/nuclei.
 <p align="center">
 <img src="https://user-images.githubusercontent.com/43107602/67619243-68e0ef80-f7f9-11e9-9bf1-0302d60971c6.png" width="400">
 </p>

### The barcode structure
After barcoding, a template switch is introduced, cells are lysed and the barcoded transcripts are amplified via PCR to generate a sequencing library. The barcoded transcript now contains sequencing adapters on both ends.
The three barcodes (pink, green and blue) make up the cell-specific barcode. All transcripts from the same cell are suposed to have the same barcode combination (the same cellular barcode). The brownish sequence corresponds to the UMI and allows to distinugish technical from biological replicates.

In that way, the cellular barcode (CBC) allows to group transcripts (expressed genes) to cells and the UMI allows to determine the number of biological copies of every transcript (UMI count per unique transcript).

Sequencing then produces two reads per barcoded transcipt that are stored in genomics_read.fastq and barcode_reads.fastq. Those files are used in the processing of raw reads in the pipeline developed (as described below).
 <p align="center">
  <img src="https://user-images.githubusercontent.com/43107602/67618927-bf4c2f00-f7f5-11e9-8724-719dcf57a3c4.png"  width="500">
 </p>

## PIPELINE: Sequencing read analysis
### Create barcode combinations
At first, three files (.txt) have to be created that contain the barcodes used in each round of the SPLiT-seq experiment. Those files are used to create a file (.txt) that contains all possible combinations of CBC's. Every possible CBC sequence is composed of three parts - a barcode from the 1st round, 2nd round and 3rd round of barcoding.

### Filter mate reads
The next step is the selection of valid barcodes (barcode_reads.fastq) and their corresponding mate reads (genomic_reads.fastq). In the first step, every read in the "barcode_reads.fastq" file is parsed, and the actual barcodes (8 bp long sequence) are extracted from the whole read that contains linkers (grey bars). Those CBC's are stored internally together with the read quality information from the original .fastq file.
Next, every CBC is "aligned" to the reference file that contains all possible CBC combinations. Here one of two options can be choosen when executing this step.

**Comprehensive alignment:**
This option tries to find matches in the reference for every BC read up to an edit distance (ED) of <= 5. A record is kept for each aligned BC read that stores its alignment position(s) in the reference, the edit distance(s) (ED) to every aligned  sequence and the number of aligned reads with EDs 0 to 5. A comprehensive output statistic and alignment summary is returned to the user. This option is very memory and time intensive. It should only be used on a small portion (~ 5 Mio reads) of the sequencing reads to get an idea of the structure and quality of the performed experiment.

**Fast alignment:**
This option tries to find matches in the reference for every BC read with ED <= 1. This type of alignment returns a list that contains every BC read and infromation on wether it could be aligned or not. This fast alignment is useful to perform BC read selection on a bigger amount of reads (80 Mio reads or more).

In both alignment versions, the next step is to mark BC reads that have a UMI with a Phred32 quality score > 10. Laslty, BC reads together with their mate read in the genomic_read.fastq file are extracted and written to three files based on the quality of the CBC and UMI of the BC read. Selected genomic reads are written to filtered_genomic_reads.fastq, selected BC reads are written to filtered_BC_reads.txt and the corresponding UMIs are written to filtered_UMIs.txt.

### Align to reference genome
The filtered genomic reads (filtered_genomic_reads.fastq) are aligned to a reference genome with the STAR aligner (the file aligned_filtered_genomic_reads.sam is obtained). Before that, a STAR Index file of the reference genome has to be created. 

### Add gene names
The aligned genomic reads have to be associated with the name of the gene that they could be aligned to. This is done by using the Drop-seq program "TagReadWithGeneFunction", which adds a tag to the aligned_filtered_genomic_reads.sam file that specifies the gene name of every aligned genomic read.

### Add CBC and UMI
In this step, every aligned genomic read is associated with its CBC and UMI in form of a tag.

### Calculate DGE matrix
In the last step, UMIs of all reads are collapsed and reads are clustered according to their CBC. This is done using the Drop-seq program "DigitalExpression", which produces a DGE matrix that contains all CBCs from the experiment (cells) as columns and all existing genes as rows. The cells of this matrix contain the UMI count of every transcript within every cell (BC combination). This UMI count expresses the expression level of each gene within a particular cell. 
 
 <p align="center">
  <img src="https://user-images.githubusercontent.com/43107602/68235158-08c12900-0003-11ea-9335-7b24cceb49bc.png"  width="700">
 </p>

# Credit
All graphics and content in "BACKGROUND: The SPLiT-seq experiment" are based on the paper from Rosenberg et al.(1)

# References
1) Rosenberg, A. B. et al. Single-cell profiling of the developing mouse brain and spinal cord with split-pool barcoding. Science (80-. ). 360, 176 LP – 182 (2018).
