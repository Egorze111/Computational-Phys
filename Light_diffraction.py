"""
Assignment 4
Exercise 5.4: diffraction telescope
When you look at light through a telescope, a point will diffract into a set of concentric rings
Given the equation for this diffraction, write a program that calculates the Bessel function inside the equation and plot the Bessel function and the light diffraction
"""

from numpy import pi, sin, cos, arange, zeros, sqrt
from matplotlib.pyplot import plot, show, imshow, legend, hot


n = 1000
h = pi / n
a = 0
b = pi

def f(m,x,theta):
    return cos(m*theta - x*sin(theta))
    # calculates the function

## finds the bessel function
def J(m,x):
    answer = f(m,x,a) + f(m,x,b)
    for k in range(1, n, 2):
        answer += 4 * f(m,x, a + k*h)
    for k in range(2,n,2):
        answer += 2 * f(m,x, a + k*h)
    return answer * h / (3 * pi)

## plot the bessel functions at m=0,1,2
for m in range(3):
    y_values = []
    x_values = []
    for x in arange(0,20,.1):
        x_values.append(x)
        y_values.append(J(m,x))
    plot(x_values, y_values, label=m)
legend()
show()

#######################################
### part b:
### use the J function to make a density plot of the light diffraction
###################################

## make an array to hold the data
integral = zeros([201,201],float)
side = 201
x1 = side/2
y1 = side/2
wavelength = 500
k = 2 * pi / wavelength

#loop through points in the array
for y in range(201):
    for x in range(201):
        # find the distance from the center at any point in the array
        r = sqrt((x-x1)**2 + (y-y1)**2)
        # calculate the bessel function for the integral
        j1 = J(1, k * r)
        # calculate the integrals
        integral[y,x] = (j1 / (k * r))**2

# graph the array
imshow(integral, origin="lower")
hot()
show()
