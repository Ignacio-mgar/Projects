import numpy as np
import matplotlib.pyplot as plt

n = 400
y = 72
theta = np.arange(0.01,1,0.01)

def likelihood(n,y,theta):
    return(theta**y*(1-theta)**(n-y))

plt.plot(theta,likelihood(n, y, theta))
plt.axvline(x=y/n)
plt.ylabel("Likelihood")
plt.xlabel("Theta")
plt.show()
plt.clf()

def loglike(n,y,theta):
    return(np.log(theta)*y+np.log(1-theta)*(n-y))

plt.plot(theta,loglike(n,y,theta)) 
plt.axvline(x=y/n)
plt.ylabel("Log-likelihood")
plt.xlabel("Theta")
plt.show()
plt.clf()