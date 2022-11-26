"""
Assignment 10: Exercise 8.3
A) Write a program to solve the equations and plot y as a function of time.
B) plot z against x(the butterfly plot)
"""

from numpy import arange, array
import matplotlib.pyplot as plt

## A
sigma = 10
r = 28
b = 8/3
t_initial = 0
t_final = 50
x_start = 0
y_start = 1
z_start = 0

def f(g):
    y = g[1]
    z = g[2]
    x = g[0]
    fx = sigma * (y - x)
    fy = r*x - y -x*z
    fz = x*y - b*z
    return array([fx, fy, fz], float)

N = 10000
h = (t_final-t_initial) / N

t_points = arange(t_initial, t_final, h)
x_points = []
y_points = []
z_points = []

q = array([x_start,y_start,z_start], float)
for t in t_points:
    x_points.append(q[0])
    y_points.append(q[1])
    z_points.append(q[2])
    k1 = h*f(q)
    k2 = h*f(q+0.5*k1)
    k3 = h*f(q+0.5*k2)
    k4 = h*f(q + k3)
    q += (k1 + 2*k2 + 2*k3 +k4)/6

## plot y vs t
plt.subplot(211)
plt.plot(t_points, y_points)
plt.xlabel("time")
plt.ylabel("y values")

## B-- plot z vs x
plt.subplot(212)
plt.plot(x_points, z_points)
plt.xlabel("x points")
plt.ylabel("z_points")
plt.show()