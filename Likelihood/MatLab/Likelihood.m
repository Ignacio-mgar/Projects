
function [ L ] = Likelihood(n, y, theta)
L = (theta.^y.*(1-theta).^(n-y));
end

