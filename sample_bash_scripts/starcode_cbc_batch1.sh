inp="/Users/manuel/Desktop/filtered_bc_reads_1mio.txt"
out="/Users/manuel/Desktop/clustered_barcodes.txt"

starcode \
     --threads 4 \
     --input $inp \
     --output $out \
     -d 4 \
     -r 1 \
     --seq-id
     
#     --print-clusters
