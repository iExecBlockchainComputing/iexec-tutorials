library("crypto")

# From https://github.com/JesseVent/crypto
dat=list()

btc <- crypto_history("btc")
rlc <- crypto_history("rlc")
snm <- crypto_history("snm")
gnt <- crypto_history("gnt")

currentdate<-gnt[dim(gnt)[1],c("date")]
write.csv(btc, file="btc.csv")
write.table(rlc, file="rlc.dat",sep=",", col.names = FALSE)
write.table(snm, file="snm.dat",sep=",", col.names = FALSE)
write.table(gnt, file="gnt.dat",sep=",", col.names = FALSE)

dataset_file<-paste("cloudcoin", currentdate, sep="_")
dataset_file <- paste(dataset_file,"csv", sep=".")
cmd =paste("cat btc.csv rlc.dat snm.dat gnt.dat ",dataset_file, sep=">")
system(cmd)
system("rm btc.csv rlc.dat snm.dat gnt.dat")
