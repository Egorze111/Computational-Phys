"""
Assignment 6: Quantum uncertainty in harmonic oscillator
A) Given the wave function psi, write a funcion to calculate the Hermite Polynomial for x and n>= 0
Plot the wave function for n = 0,1,2,3 and -4<=x<=4
B) make a separate plot for n = 30  and -10<= x <=10
C) evaluate an integral using gaussian quadrature and calculate the uncertainty when n = 5
"""

from numpy import sqrt, Inf, zeros
from math import factorial, pi, exp
from matplotlib.pyplot import plot, show, legend
from derivatives.gaussxw import *


## function for Hermite Polynomial
def H(n,x):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    H_old = 2 * x
    H_current= 4 * x**2 - 2
    for i in range(1, n-1): ## or while?    
        h_new = 2*x*H_current - 2*(i+1)*H_old
        H_old = H_current
        H_current = h_new
    return H_current

def find_psi(n,x):
    return (1 / (sqrt((2 ** n) * factorial(n) * sqrt(pi)))) * exp((-x ** 2) / 2) * H(n,x)
N = 100
psi = zeros([N],float)
X = linspace(-4, 4, N)

for n in range(0,4):
    i = 0
    for x in X:
        psi[i] = find_psi(n,x)
        i += 1
    plot(X, psi, label=i) # ok so now something plots
legend()
show()   

"""
part b: the BIG test
"""
N = 1000
psi = zeros([N],float)
X = linspace(-10, 10, N)

for n in range(30,31):
    i = 0
    for x in X:
        psi[i] = find_psi(n,x)
        i += 1
    plot(X, psi, label=i)
legend()
show() 

"""
part c: solve the integral with gaussian quad and square the value to find the uncertainty
when n = 5 and x is negative infinity to positive infinity.
"""
a = -8
b = 8
gaussqn = 100
s = 0
n = 5

# define the uncertainty
def f(n,x):
    f = (x ** 2) * (abs(find_psi(n,x)) ** 2)
    return f

## find the integral
xp,wp = gaussxwab(gaussqn, a, b)
for k in range(gaussqn):
    s += wp[k] * f(n,xp[k])

print(f"The integral is: {s}")

## solve for uncertainty
uncert = sqrt(s)
print(f"The uncertainty is {uncert}")
