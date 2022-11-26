"""
In-Class 22
Part a) reproduce example 9.1 (solution of Laplace's eq.)
b) reproduce the first 5 Bessel functions
"""
from numpy import empty, zeros, max, linspace
import matplotlib.pyplot as plt
from math import factorial

## known vars
M = 50 # grid squares
V = 1.0 # voltage at the top and bottom
error = 1e-6 # target error

## arrays for potential values
phi = zeros([M+1,M+1], float)
phi[0,:] = V
phi[M,:] = V
phinew = empty([M+1,M+1], float)

delta = 1.0
while delta > error:
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or i==M or j==0 or j==M:
                phinew[i,j] = phi[i,j]
            else:
                phinew[i,j] = (phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])/4
    delta = max(abs(phi- phinew))
    phi, phinew = phinew, phi

plt.imshow(phi,origin='lower')
plt.jet()
plt.colorbar()
plt.show()

#####################
##### part b ########
#####################

z = linspace(0,20,100)
## n goes from 0 to 5

def gamma(m):
    return factorial(m-1)

def J(n,z):
    bessel = 0
    for m in range(35):
        bessel += ((-1)**m)/(factorial(m) * gamma(m+n+1)) * (z/2)** (2*m +n)
    return bessel

title = ["J0","J1","J2","J3","J4"]

i = 0
for n in range(5):
    bessel = J(n,z)
    plt.plot(bessel,label=title[i])
    i += 1

plt.legend()
plt.xlabel("Bessel functions")
plt.show()