"""
In-class assignment 19
"""
from numpy import sin, cos, array, arange, pi, linspace, ones
import matplotlib.pyplot as plt

## use the code on pg. 350 and 4th Runge-Kutta to plot theta vs. time for a half cycle
g = 9.81
l = 1.5

def f(r):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta, fomega], float)

a = 0.0
b = 10.0
N = 10000
h = (b-a)/N

angle = 60
speed = 0

t_vals = arange(a,b,h)
x_vals = []
y_vals = []
x = array([angle * pi / 180,speed],float)

for t in t_vals:
    x_vals.append(x[0])
    y_vals.append(x[1])
    k1 = h*f(x)
    k2 = h*f(x+0.5*k1)
    k3 = h*f(x+0.5*k2)
    k4 = h*f(x + k3)
    x += (k1 + 2*k2 + 2*k3 +k4)/6

plt.subplot(121)
plt.plot(t_vals, x_vals)
plt.plot(t_vals, y_vals)
plt.xlabel("time")
plt.ylabel("theta")

plt.subplot(122)
plt.plot(x_vals, y_vals)
plt.xlabel("angular position")
plt.ylabel("angular velocity")

plt.show()

"""
Mathematical:
graph the first 6 Legendre polynomials
"""

x = linspace(-1,1,N)

p0 = ones((10000),float)
p1 = x
p2 = 0.5*(3*x**2 - 1)
p3 = 0.5*(5*x**3 - 3*x)
p4 = 0.125 * (35*x**4 - 30*x**2 + 3)
p5 = 0.125 * (63*x**5 - 70*x**3 + 15*x)

plt.plot(x, p0, label="P0(x)")
plt.plot(x, p1, label="P1(x)")
plt.plot(x, p2, label="P2(x)")
plt.plot(x, p3, label="P3(x)")
plt.plot(x, p4, label="P4(x)")
plt.plot(x, p5, label="P5(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("Pn(x)")
plt.show()