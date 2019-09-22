# basic setup
n <- 1000
a <- 0
b <- 0
p <- 1/2
x <- rep(0,n)
cut_a <- 11
cut_b <- 11


# Make n simulations
for(i in 1:n) {
    # remember to reset a and b between simulations
    a <- 0
    b <- 0
    # the individual repair simulation
    while ((a < cut_a) and (b < cut_b)) {
        # a repair where we use either 1 'a' or 1 'b'
        t <- sample(0:1, 1, prob=c(1-p,p))
        if (t == 0) { a <- a + 1 } else { b <- b + 1 }
        # are we done? If so then either a or b is at the cut-off
        if (a == cut_a) { x[i] <- b }
        if (b == cut_b) { x[i] <- a }
    }
}
# Make a summary table and a histogram of the distribution
table(x)
hist(x, breaks=seq(0,11,by=1))
