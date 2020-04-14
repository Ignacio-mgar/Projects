function [ l ] = Loglike( n,y,theta )

l=log(theta)*y+log(1-theta)*(n-y);
end

