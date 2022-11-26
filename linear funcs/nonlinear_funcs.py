"""
In-class Assignment 14:
Use the relaxation, binary search, and Newton's 
methods to find the solution to the given equation. 
"""

from math import exp

"""
Relaxation Method
"""
# function to calculate the x-values
def f(x):
    x_new = 5 - 5 * exp(-x)
    return x_new
    ## type type type type type type type type type type type type type

# derivative of f(x)
def fprime(x):
    return 1 - 5 * exp(-x)

def calc_error(x, new_x):
    return (x - new_x) / (1 - (1 / fprime(x)))

# assign a value to x
x = 1.0
error = 1.0
acc = 1e-6
count = 0

while abs(error) > acc:
    x_new = f(x)
    error = calc_error(x, x_new)
    x = x_new
    count += 1

print()
print("RELAXATION METHOD:")
print(f"Initial x: 1  Final answer: {x}  Number of iterations: {count}")

"""
Binary Search
will use:
acc value
"""

def func(x):
    return 5 * exp(-x) + x - 5

## determine the window
x1 = 2
x2 = 7
fx1 = func(x1)
fx2 = func(x2)
count = 0
error = 1
acc = 1e-6

## loop to calculate the thing
if (fx1 * fx2) < 0:
    while abs(error) > acc:  
        x_mid = 0.5 * (x1 + x2)
        midpoint = func(x_mid)
        if midpoint > 0 and fx1 > 0:
            x1 = x_mid
        elif midpoint > 0 and fx1 < 0:
            x2 = x_mid
        elif midpoint < 0 and fx1 > 0:
            x2 = x_mid
        elif midpoint < 0  and fx2 < 0:
            x2 = x_mid
        elif midpoint < 0 and fx2 > 0:
            x1 = x_mid
        elif midpoint > 0 and fx2 <0:
            x1 = x_mid
        error = x1 - x2
        count += 1
last_mid = 0.5 * (x1 + x2)

# show data
print()
print("BINARY SEARCH")
print(f"Initial range: x = 2 - 7  Final answer: {last_mid}  Number of iterations: {count}")

"""
Newton's method
Carry over func, fprime functions, acc value
"""
## reset values
error = 1
x = 7
count = 0

## calculate!
while error > acc:
    new_x = x - (func(x) / fprime(x))
    error = abs(x - new_x)
    x = new_x
    count += 1
# present data
print()
print("NEWTON'S METHOD:")
print(f"Initial x: 7  Final answer: {x}  Iterations: {count}")
