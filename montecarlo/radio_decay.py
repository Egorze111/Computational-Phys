"""
Assignment 13:
Write a program to simulate the decay of Bismuth 213
to Bismuth 209
"""

from random import random
from numpy import arange
import matplotlib.pyplot as plt

## Constants
Nbis = 10000 ## Number of Bi 213
Ntl = 0      ## Number of Tl 209
Npb = 0      ## Number of Pb 209
Nbis_final = 0# Number of Bi 209
dt = 1 #second
tmax = 20000 ## seconds

bis_tau = 46 * 60 # Bi 213 half-life in sec
tl_tau = 2.2 * 60 # Tl 209 half-life in sec
pb_tau = 3.3 * 60 # Pb 209 half-life

# lists for graphing purposes
tpoints = arange(0.0, tmax, dt)
Bispoints = []
Tlpoints = []
Pbpoints = []
finalBis = []

# to calculate tau bc there's multiple elements
def prob(tau):
    return 1 - 2** (-dt / tau)

for t in tpoints:
    ## add the points to the lists for graphing
    Bispoints.append(Nbis)
    Tlpoints.append(Ntl)
    Pbpoints.append(Npb)
    finalBis.append(Nbis_final)

    ## Calculate decay ## make this a function?
    decay = 0
    for i in range(Npb):
        if random()<prob(pb_tau):
            decay += 1
    Npb -= decay
    Nbis_final += decay
    decay = 0
    for i in range(Ntl):
        if random()<prob(tl_tau):
            decay += 1
    Ntl -= decay
    Npb += decay
    decay = 0
    for i in range(Nbis):
        if random()<prob(bis_tau):
            decay += 1
    Nbis -= decay
    for i in range(decay):
        if random()<0.9791:
            Npb += 1
        else:
            Ntl += 1

# plot the different elements!
plt.plot(tpoints, Bispoints, label="Bi 213")
plt.plot(tpoints, Tlpoints, label="Tl 209")
plt.plot(tpoints, Pbpoints, label="Pb 209")
plt.plot(tpoints, finalBis, label="Bis 209")
plt.legend()
plt.xlabel("Time(seconds)")
plt.ylabel("# of molecules")
plt.show()