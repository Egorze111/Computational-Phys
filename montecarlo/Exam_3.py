"""
Exam 3:
"""
from numpy import arange, linspace, array, zeros, empty, zeros_like
import matplotlib.pyplot as plt
from math import factorial
from random import random

"""
Problem 1:
model a damped spring-mass system with three
different damping coeffs
"""

# ### Constants ###
# mass = 25 # kg
# k = 16 # N/m
# c1 = 4
# c2 = 40
# c3 = 200
# v_initial = 0
# h = 0.1
# c_list = [c1,c2,c3]

# time = arange(0,30,0.1)

# def f(r,c):
#     x = r[0]
#     v = r[1]
#     dx = v
#     dv = (-c*v - k*x) / mass
#     return array([dx,dv], float)
# for c in c_list:
#     x_points = []
#     x = array([1.5,v_initial],float) # meters
#     for t in time:
#         x_points.append(x[0])
#         k1 = h*f(x,c)
#         k2 = h*f(x+0.5*k1,c)
#         k3 = h*f(x+0.5*k2,c)
#         k4 = h*f(x+k3,c)
#         x += (k1+ 2*k2 + 2*k3 + k4) / 6

#     plt.plot(time, x_points, label=f"damping: {c}")

# plt.xlabel("time")
# plt.ylabel("displacement")
# plt.legend()
# plt.show()

"""
Problem 2:
Use overrelaxation and Gauss-Sidel to plot a density plot
of electric potentials inside a metal box
"""
## known vars
M = 100 # grid squares
V = 1.0 # voltage at the top and bottom
error = 1e-6 # target error
step = 10/M
omega = 0.7 ## random guess
## little bit of thinking to figure out that the bars
## start at the 20th step and end at the 80, at column 20 and 80

## arrays for potential values
phi = zeros([M+1,M+1], float)
phi[20:80,20] = V # first plate
phi[20:80,80] = -V # second plate

delta = 1.0
while delta > error:
    for i in range(M+1):
        for j in range(M+1):
            if i in range(20,80) and j==20 or j==80:
                phi[i,j] = phi[i,j]
            elif i==0 or i==M or j==0 or j==M:
                phi[i,j] = phi[i,j]
            else:
                phi[i,j] = ((phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])* (1+omega)/4) - omega*phi[i,j]
            delta = phi[i,j] - phi[i,j-1]

plt.imshow(phi,origin='lower')
plt.jet()
plt.colorbar()
plt.show()
## I think that's right? It doesn't look like I expected it to,
# but maybe that's okay? It looks similar to what I got for Assign 22

"""
Problem 3:
Write a program to simulate the dropping of 100000 balls
into an arrangement of pins and make a bar graph of the distribution.
"""
# N = 100000
# probab = 0.5

# yvals = zeros(7,int) ## for the graph
# xvals = linspace(-3,4,7)


# for n in range(N):
#     peg = 0
#     for i in range(6): ## for each row
#         if random() > probab:
#             peg += 1
#         else:
#             peg -= 1

#     yvals[peg] += 1

# plt.bar(xvals, yvals, width=0.5, edgecolor="white")
# plt.xlabel("Bin number")
# plt.ylabel("# of balls")
# plt.show()

## The graph doesn't look right, but I think I kind of got
## the concept right

"""
Problem 4:
Write a given equation in terms of Legendre Polynomials
Plot a table of Bessel functions
"""
## see part a in the paper
## plotting bessel funcs

##x = arange(0,13,0.1)
##
##def gamma(m):
##    return factorial(m-1)
##
##def J(n,z):
##    bessel = 0
##    for zval in z:
##        for m in range(35):
##            if zval>=12:
##                zval=0
##            bessel += ((-1)**m)/(factorial(m) * gamma(m+n+1)) * (z/2)** (2*m +n)
##    return bessel
##
##title = ["J0","J1","J2"]
##
##i = 0
##for n in range(3):
##    bessel = J(n,x)
##    plt.plot(bessel,label=title[i])
##    i += 1
##
##plt.legend()
##plt.xlabel("Bessel functions")
##plt.show()

## I'm not sure if this graph is right, but it looks like bessel functions