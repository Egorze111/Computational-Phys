"""
In-Class 24
Write a Python program that simulates the rolling 
of two dice. Roll the dice 1,000,000 times and 
produce a histogram of the sum of the two dice. 
Compare your histogram to the theoretical 
distribution. 
"""

from random import randrange
from numpy import array, zeros, linspace
import matplotlib.pyplot as plt

## Constants
rolls = 1000000
p2=p12 = 1/36*rolls
p3=p11 = 1/18*rolls
p4=p10 = 1/12*rolls
p5=p9 = 1/9*rolls
p6=p8 = 5/36*rolls
p7 = 1/6*rolls
prbs = array([p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12],float)
# roll_2 = []
yvals = zeros(11,int)
xvals = linspace(2,12,11)

def roll_dice():
    roll = randrange(1,7,1)
    return roll

for i in range(rolls):
    totval = roll_dice() + roll_dice()
    yvals[totval-2] += 1
        
plt.bar(xvals, prbs, width=0.45, align="edge", label="Predicted", edgecolor="white")
plt.bar(xvals, yvals, width=-0.45, align="edge",label="Experiment", edgecolor="white")
plt.legend()
plt.xlabel("Dice roll")
plt.ylabel("# of rolls")
plt.show()
