"""
Assignment 12: exercise 9.4, page 424
Write a program to calculate the temp profile 
of the crust of the earth
"""
from numpy import sin, pi, empty, linspace
import matplotlib.pyplot as plt

# Constants
tao = 365 # days
A = 10 # degrees Celcius # coldest temp
B = 12 # degrees Celcius # hottest temp thing
D = 0.1 # m^2 /day # thermal diffusion
temp_bottom = 11 # degrees Celcius
bottom = 20
time = linspace(0, 3650, 3650) ## total time = 10 years
dx = 0.5 # meters ## can also be changed to 0.4 if 0.5 is too big or is too glitchy
dt = 1 # days
N = int(20/dx)
t1 = 3376
t2 = 3468
t3 = 3559
t4 = 3650
epsilon = dt/10

def surface_temp(t):
    return A + B * sin(2*pi*t/tao)

## create arrays
temps = empty(N+1,float)
temps[0] = temp_bottom
temps[N] = surface_temp(0)
temps[1:N] = A

new_temps = empty(N+1,float)
new_temps[0] = temp_bottom
new_temps[N] = surface_temp(0)

# do the calculation 
c = dt * D / dx**2
#print(time)
for t in time:
    #print(t)
    new_temps[N] = surface_temp(t)
    new_temps[1:N] = temps[1:N] + c * (temps[2:N+1] + temps[0:N-1] - 2*temps[1:N])
    temps, new_temps = new_temps, temps
    if abs(t-t1) < epsilon:
        plt.plot(temps,"r-",label="Summer")
        print(abs(t-t1))
    if abs(t-t2) < epsilon:
        plt.plot(temps, color="darkorange",label="Fall")
        print(abs(t-t2))
    if abs(t-t3) < epsilon:
        plt.plot(temps,"b-",label="Winter")
        print(abs(t-t3))
    if abs(t-t4) < epsilon:
        plt.plot(temps,"g-",label="Spring")
        print(abs(t-t4))
plt.legend()
plt.xlabel("Depth")
plt.ylabel("Temperature")
# plt.xlim(right=21)
# plt.ylim(7,13)
plt.show()
