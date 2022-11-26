"""
Assignment 5: activity 5.7, page 162
Given an integral, find the value of the integral using:
a) adaptive trapezoidal method
b) adaptive simpson's method
c) Romberg integration
"""
# import libraries
from numpy import sin, sqrt, zeros
from datetime import datetime

# define constants and important values
error = 1
N = 1
a = 0
b = 1
h = 1 # (b-a) / N 

# define the function of the given equation
def f(x):
    """
    computes the inside part of the given integral to evaluate
    Parameters:
        x- location on the x-axis to determine the value of the curve
    """
    return (sin(sqrt(100 * x)))**2
 
"""
Part a: Trapezoidal Method
"""
def find_trap_method():
    """
    computes an integral using the trapezoidal method to a given error value. 
    Parameters:
        none
    Return:
        N- how many steps to get the given error
        I- the value of the integral
        error- the final error value that ends the while loop.
    """
    # define start time to measure efficiency
    start_trap = datetime.now()
    
    # calculate the initial integral value
    I_old = .5 * f(a) + 0.5 * f(b)
    global h
    global N
    global error

    # loop to compute the integral to a given accuracy
    while abs(error) > 1e-6:
        h /= 2
        N *=2
        s = 0
        for k in range(1,N,2):
            s += f(a + k*h)
        I = .5 * I_old + h * s
        error = (I - I_old) / 3
        I_old = I
    print("Adaptive Trapezoidal Method:")
    print(f"N value: {N}, Integral: {I}, error: {error}")
    print(datetime.now() - start_trap)

"""
part B: compute the same integral f(x) using the simpson's method
"""
def compute_simp_method():
    """
    calculate an integral using Simpson's method
    Parameters:
        none
    Return:
        N- how many steps to get the given error
        I- the value of the integral
        error- the final error value that ends the while loop.
    """
    # define the start time and redefine h, N, and the error from the trap. method
    start_simp = datetime.now()
    h = .5
    error = 1
    N = 2

    # calculate the initial Integral value
    s = (f(a) + f(b)) / 3
    tsum = f(h) * 2 / 3
    I_old = h * (s + 2 * tsum)

    # loop to compute the integral to a given accuracy
    while abs(error) > 1e-6:
        N *= 2
        h /= 2
        t = 0
        sum_new = s + tsum
        for k in range(1, N, 2):
            t += f(a + k*h)
        tsum = t * 2 / 3
        I = h * (sum_new + 2 * tsum)
        error = (I - I_old) / 15
        I_old = I
        s = sum_new
    print("Adaptive Simpson's Method:")
    print(f"N value: {N}, Integral: {I}, error: {error}")
    print(datetime.now() - start_simp)

"""
Part c: Romberg integration
"""
start_rom = datetime.now()
def romberg_int():
    """
    computes an integral using Romberg Integration to a given error value. 
    Parameters:
        none
    Return:
        The pyramid of R values(or the integral values)
    """
    print("Romberg Integration:")
    # Constants
    a = 0
    b = 1
    N = 1
    error = 1
    R = zeros([8,8], float)
    
    # Compute an initial estimate for the integral    
    R[1,1] = 0.5*f(a) + 0.5*f(b)
    print(R[1,1])
    e = 1
    i = 2

    # loop to compute the integral to a given accuracy
    while abs(e) > 1e-6:
        N *=2
        h = (b - a)/N
        s = 0
        # Use the trapezoidal rule fill this in for adaptive Trap method, and update R
        for k in range(1,N,2):
            s+= f(a + k*h)
        R[i, 1] = h*s + 0.5*R[i-1,1]
        print(R[i, 1],end=' ')

        # Compute the Romberg coefficients
        for m in range(1,i):
            e = (R[i,m] - R[i-1,m]) / (4**m -1)
            R[i,m+1] = R[i,m] + e
            print(R[i, m+1],end=' ')
        print(' ')
        i +=1

    print(datetime.now() - start_rom)   

def main():
    find_trap_method() 
    compute_simp_method()
    romberg_int()

## runs each method and prints the integral value, amount of steps needed
## and the time it took to run each function
main()