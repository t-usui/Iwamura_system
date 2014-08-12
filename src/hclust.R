args <- commandArgs(trailingOnly=T)
infile <- args[1]
outfile <- args[2]
d <- as.dist(read.csv(infile, row.names=1))
hc <- hclust(d)
library(ctc)
write.table(hc2Newick(hc), file=outfile, row.names=FALSE, col.names=FALSE)
