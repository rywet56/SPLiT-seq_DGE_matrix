#inp="/Users/manuel/Desktop/filtered_UMIs_2mio.txt"
#out="/Users/manuel/Desktop/clustered_UMIs.txt"

inp="/Users/manuel/Desktop/bowtie_strategy/selected_umis.txt"
out="/Users/manuel/Desktop/bowtie_strategy/clustered_UMIs.txt"

starcode \
     --threads 4 \
     --input $inp \
     --output $out \
     -d 1 \
     -r 1 \
     --seq-id
     
     
#     --print-clusters


# d --> number of differences at which sequences diverge into different clusters
