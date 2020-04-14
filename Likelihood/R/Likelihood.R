likelihood <- function(n,y,theta){return(theta^y*(1-theta)^(n-y))}
loglike <- function(n,y,theta){return(log(theta)*y+log(1-theta)*(n-y))}
n <- 400
y <- 72
theta <- seq(0.01, 0.99, 0.01)
plot(theta, likelihood(n,y,theta),"l")
abline(v=y/n)

plot(theta, loglike(n,y,theta),"l")
abline(v=y/n)