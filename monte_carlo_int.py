"""
Last In-class assignment!
Construct a M.C. simulation of throwing darts at a board.
Let N be 1 million
a)what is the expected value for the ratio?
    is gonna be .25*pi, or 0.785398(Area of the circle over area
    of the square, which is 1)
b) give the value of the ration with uncertainty
"""

from numpy import sqrt, zeros, std
from random import random

##I'm going to just calculate the area of the first quadrant, for simplicity
def f(x):
    return sqrt(0.25 - x**2)

N = 1000000
n = 0 # dummy var for looping purposes
integrals = zeros(10,float)

while n<10:
    count = 0
    for i in range(N):
        x = 0.5*random() ## to stay inside the first quadrant
        y = 0.5*random()
        if y<f(x):
            count += 1
    I = count/N ## the four to make it a circle is cancelled out by the area of the quadrant
    print(I)
    integrals[n] = I
    n += 1

## to calculate uncertainty:
# to get the average
total = 0
top = 0

for num in integrals:
    total += num
avg = total / len(integrals)
print(avg)
# print(integrals)

# function of sigma
def calc_sigma(top):
    return sqrt(top / (10-1))

for x in integrals:
    top += (avg - x)**2

print(f"The uncertainty is {calc_sigma(top)}") 
## I was having issues with the calculation, hence the function below and above.

print(f"Sigma with numpy: {std(integrals)}")
