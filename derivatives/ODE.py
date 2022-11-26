"""
In-class Assignment 18:
Solve the given differential equation with:
A) Euler's Method
B) Second-Order Runge-Kutta
C) Fourth-Order Runge-Kutta
"""
from math import log
from numpy import arange
import matplotlib.pyplot as plt

## the actual solution to compare answers:
sol = 25 / (4 + 3*log(2) - 3*log(5))

# define the ODE
def f(x,t):
    return (2*x/t) + (3*x**2/t**3)

## we know that x=1 when t=2, and we want x when t = 5. N = 100

"""
A) Euler's Method
"""
# define start and stop
a = 2.0
b = 5.0
N = 100
h = (b-a)/N
x = 1.0

## calculate!!
t_values = arange(a,b+(h/2),h)
x_values = []
for t in t_values:
    x_values.append(x)
    x += h * f(x,t)

# # plot the results?
# plt.plot(t_values, x_values)
# plt.xlabel("t")
# plt.ylabel("x(t)")
# plt.show()

# calculate the percent difference
diff = (x - sol) / sol
percent = diff * 100
print(f"value: {sol}")
print(f"Euler: {x} difference: {percent:.3f} %")

"""
B) Runge-Kutta 2nd
"""
## keep the initial values from A
tpoints = arange(a,b+h/2,h)
xipoints = []

xi = 1.0

for t in tpoints:
    xipoints.append(xi)
    k1 = h*f(xi,t)
    k2 = h*f(xi+0.5*k1, t+0.5*h)
    xi += k2

# calculate the percent difference
diff = (xi - sol) / sol
percent = diff * 100
print(f"2nd Runge-Kutta: {xi} difference: {percent:.3f} %")

"""
C) 4th Runge-Kutta
"""
## keep initial values again
t_nums = arange(a,b,h)
x_nums = []
xr = 1.0
#print(t_nums)
for t in t_nums:
    x_nums.append(xr)
    k1 = h*f(xr, t)
    k2 = h*f(xr+0.5*k1, t+0.5*h)
    k3 = h*f(xr+0.5*k2, t+0.5*h)
    k4 = h*f(xr + k3, t+h)
    xr += (k1 + 2*k2 + 2*k3 +k4)/6

# calculate the percent difference
diff = (xr - sol) / sol
percent = diff * 100
print(f"4th Runge-Kutta: {xr} difference: {percent} %")

