inp="/Users/manuel/Desktop/bowtie_strategy/selected_barcodes.txt"
#inp="/Users/manuel/Desktop/bowtie_strategy/test.txt"
out="/Users/manuel/Desktop/bowtie_strategy/clustered_barcodes.txt"

starcode \
     --threads 4 \
     --input $inp \
     --output $out \
     -d 1 \
     -r 1 \
     --seq-id \
     --print-clusters
