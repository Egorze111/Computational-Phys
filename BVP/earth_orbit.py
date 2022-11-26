"""
Assignment 11:Orbit of the Earth
Use the verlet method to calculate the orbit of the Earth around the Sun
A) calculate using the Verlet method and plot the orbit of the earth for a few years
B) add calculations for PE, KE, and total energy and graph them together over time.
C) plot just the total energy 
"""

from numpy import array, arange
import matplotlib.pyplot as plt

## define variables
G = 6.6738e-11    ## gravitational constant
M = 1.9891e30     ## mass of the sun
m = 5.9722e24     ## mass of the earth
h = 3600          ## 1 hour, in seconds
r = array([0, 1.471e11],float)     ## meters
v = array([3.0287e4, 0],float)     ## m/s
t_start = 0
t_final = 3*365*24*h ## seconds in a year, times 3 years
time = arange(t_start, t_final,h) # total time, measuring once an hour

x=[]
y=[]
PE = []
KE = []
TE = []

def f(r):
    radius = (r[0]**2 + r[1]**2)**0.5
    ddx = -G*M*r[0]/radius**3
    ddy = -G*M*r[1]/radius**3
    return array([ddx,ddy], float)

## equation 8.77
v = v + 0.5*h*f(r)

for t in time:
    r += h*v
    k = h*f(r)
    x.append(r[0])
    y.append(r[1])
    ## calculate PE
    radius = (r[0]**2 + r[1]**2)**0.5
    pe = -G*M*m/radius
    PE.append(pe)
    ## calculate KE
    vmid = v + 0.5*k
    v_for_ke = (vmid[0]**2 + vmid[1]**2)**0.5
    ke = 0.5*m*v_for_ke**2
    KE.append(ke)
    ## total energy
    te = pe + ke
    TE.append(te)
    v += k
    
## plot the orbit-- part A
plt.subplot(131)
plt.plot(x,y)
#plt.plot(time,x) # just to check

##plotting part b
plt.subplot(132)
plt.plot(time,KE,label="Kinetic Energy")
plt.plot(time,PE,label="Potential Energy")
plt.plot(time,TE,label="Total Energy")
plt.xlabel("time")
plt.ylabel("Energy levels")
plt.legend()

## part c
plt.subplot(133)
plt.plot(time,TE,"g,")
plt.xlabel("time")
plt.ylabel("Total Energy")
plt.show()

## review days July 11/12?