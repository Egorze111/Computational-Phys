"""
In-class Assignment 21
A fluid goes between two fixed plates with a varying velocity(think like a river)
Use an ODE method and a root finding method to find the range of fluid velocities across the gap 
"""
from numpy import array, arange, zeros
import matplotlib.pyplot as plt

v_start = 0  # initial velocity
v_last = 0  # final velocity
a = 0
b = 0.1 # meters
viscosity = 1 ## waterrr
dp = -100 # pascals/meter
N = 1000
h = (b-a) / N
error = 1e-10

distance = arange(a,b,h)

## function to set up the ODE
def f(r):
    v = r[0]
    w = r[1] ## dummy variable to represent the second derivative of v
    dv = w
    dw = dp / viscosity ## given function from the problem
    return array([dv,dw], float)


## function to solve for velocity
def velocity(w):
    graphvx = []
    r = array([0.0,w],float)
    for d in distance:
        k1 = h*f(r)
        k2 = h*f(r + 0.5*k1)
        k3 = h*f(r+0.5*k2)
        k4 = h*f(r+k3)
        r += (k1 + 2*k2 + 2*k3 +k4) / 6
        graphvx.append(r[0])  
    return r[0],graphvx

## binary search part
w1 = 0.01
w2 = 1000.0
v1,graphvx = velocity(w1)
v2,graphvx = velocity(w2)

while abs(v2-v1) > error:
    wp = (w1+w2) / 2
    vp,graphvx = velocity(wp)
    if v1*vp > 0:
        w1 = wp
        v1 = vp
    else:
        w2 = wp
        v2 = vp

w = (w1 + w2) / 2
print(f"The required change in velocity is {w} m/s^2")

## graph the dang thing
plt.plot(graphvx, distance)
plt.xlabel("change in velocity")
plt.ylabel("distance between plates")
plt.show()