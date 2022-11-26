"""
Assignment 8:
A) write a program that reads the data from sunspots.txt
and graph it as a function of time. Make an estimate of the period in months
B) calculate the fourier transform of the sunspot data and graph the 
coefficients as a function of k and of the magnitude squared
C)find the approx. value of k for the peak and use it to calculate the
period- compare it to the estimation from part a.
"""

from numpy import loadtxt, linspace, zeros
from cmath import exp, pi
import matplotlib.pyplot as plt


spots = loadtxt("week8_nonlinear\\sunspots.txt", float)

"""
part A
graph the data and estimate the period
"""
x = linspace(0, len(spots))
# len(spots) = 3143

t_spots = spots[:,0]
y_spots = spots[:,1]
plt.plot(t_spots, y_spots)
plt.xlabel("Sunspots from 1749 to 2010 by month")
plt.ylabel("Num. of Spots")

plt.show()

## still need to estimate the period-- 
## find two peaks, distance between is roughly 128 months

"""
part B:
compute the FT and plot the k values and the power function
"""

def dft(y):
    N = len(y)
    c = zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

coeff = dft(y_spots)

# plot second graph of the k space coeffients 
plt.subplot(121)
plt.plot(abs(coeff),label="k space") #note the abs value for the complex numbers c
plt.ylabel('c_k Amplitude')
plt.xlim(-5,100)
plt.xlabel('K number')
plt.legend(loc='upper right')

#plot third graph as coeff^2 function of k 
f=linspace(0,len(coeff),len(coeff))
new_coeff = coeff ** 2
plt.subplot(122)
plt.plot(f,abs(new_coeff))
plt.ylabel('c_k squared Amplitude')
plt.xlim(-5,50)
plt.xlabel('Power Spectrum')
plt.show()

"""
Part C
plot the frequencies and calculate the period
"""
scale=len(coeff)/0.5
f=linspace(0,len(coeff)/scale,len(coeff))
plt.plot(f,abs(coeff))
plt.ylabel('c_k Amplitude')
plt.xlim(0,0.01)
plt.xlabel('Frequency')
plt.show()

for i in range(1, len(coeff)):
    if abs(coeff[i])>40000:
        print('frequencies',i/scale,'1/month')
        print(f"Period: {scale/i} months")
        