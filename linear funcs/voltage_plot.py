"""
Assignment 7:
oooh boy let's go
"""

from numpy.linalg import solve
from numpy import array, sqrt, exp, linspace, zeros_like
from math import pi
from cmath import polar, phase
from matplotlib.pyplot import plot, show, legend, xlabel, ylabel

## define variables
r1 = 1000 # ohm
r2 = 2000 # ohm
r3 = 1000 # ohm
r4 = 2000 # ohm
r5 = 1000 # ohm
r6 = 2000 # ohm
c1 = 1e-6 # F
c2 = 0.5e-6 # F
x_plus = 3 # volts
omega = 1000 # Hertz
i = sqrt(-1+0j)
t_end = 4 * pi / omega

## define arrays
A = array([[((1/r1) + (1/r4) + c1 * i * omega), (-c1 * i * omega), 0],
[(-c1 * i * omega), ((1/r2) + (1/r5) + (c1 + c2) * i * omega), (-c2 * i * omega)],
[0, (-c2 * i * omega), ((1/r3) + (1/r6) + c2 * i * omega)]], complex)

v = array([[x_plus / r1],
[x_plus / r2],
[x_plus / r3]], complex)

x = solve(A,v)
print(x)
# it works! if these are the answers:
"""
[[1.69369369-0.16216216j]
 [1.45045045+0.2972973j ]
 [1.85585586-0.13513514j]]
"""
for n in range(3):
    r, theta = polar(x[n])
    phaseang = phase(x[n])
    print(r, theta * 180 / pi, phaseang)

##calculate the voltages and plot them with the initial potentials
# make arrays for the voltage at each point in the circuit
time = linspace(0,t_end,1000)
v1 = zeros_like(time)
v2 = zeros_like(time)
v3 = zeros_like(time)
v_plus = zeros_like(time)

v1 = x[0] * exp(i * omega * time)
v2 = x[1] * exp(i * omega * time)
v3 = x[2] * exp(i * omega * time)
v_plus = x_plus * exp(i * omega * time)

# plot each voltage as v+ fluctuates
plot(time,v1,"r",label="v1")
plot(time,v2, "g",label="v2")
plot(time,v3, "b",label="v3")
plot(time,v_plus,"y",label="v+")
legend()
xlabel("Time")
ylabel("Voltages")
show()
