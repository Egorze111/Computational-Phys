"""
Exam 2
"""
from math import sin, atan, pi
from numpy import linspace, arange, zeros, loadtxt
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


## about 2 hours for problem 4
## 2 hours 20 for problem 1
## maybe an hour for p. 3?
## currently 35 mins for p2

"""
Problem 1:
part a- Mathematica returns 43.7919
time taken: 2 hours 20 minutes
"""
sol = 43.7919
print(f"Evaluated Solution: {sol}")

## part b: approximate the integral with Riemann's method and 20 rectangles, using the left corner.
N = 21 # so that there is 20 rectangles?
a = 0.0
b = 4.692
h = (b-a)/N
total_area = 0

def f(x):
    return 0.2381*(x**3) - 1.231*(x**2) + 1.593*x + 8.481

for i in arange(a,b,step=h):
    left_side = f(i)
    area = left_side * h
    total_area += area
print(f"Riemann: {total_area:.4f}")

## calculate the percent error
diff = (total_area - sol) / sol
percent = diff * 100
print(f"percent error: {percent:.3f}%")

## Part c: Graph the integrand and the 20 rectangles from part b
# create arrays to graph
xx = linspace(a, b, N-1)
func = zeros([N-1], float)

i = 0
for x in xx:
    func[i] = f(x)
    # draw the rectangle
    rect = mpatches.Rectangle((x,0), h, func[i], fill=False,color="red",linewidth=1)
    i += 1
    plt.gca().add_patch(rect)
plt.plot(xx, func, label="given curve")
plt.legend()
plt.ylim(bottom=0)
plt.show()

## Part d: use Simpson's method to calculate the integral to accuracy 0.00001
# I'm gonna use adaptive simpson's because it's faster.

error = 1
# calculate the initial Integral value
s = (f(a) + f(b)) / 3
tsum = f(h) * 2 / 3
I_old = h * (s + 2 * tsum)

# loop to compute the integral to a given accuracy
while abs(error) > 1e-5:
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
print(f"N value: {N}, Integral: {I:.5f}, error: {error:.6f}")

"""
Problem 2: Electrical Current
"""
"""
Problem 3: LIGO data cleanup
"""

## a- import and graph the data
gravity = loadtxt("week10_legendre\\gravity_wave_data.txt", float)
time = linspace(0.0, 0.5, 1024)

plt.subplot(221)
plt.plot(time, gravity)
plt.xlabel("Time(seconds)")
plt.ylabel("Strain values")

## b - take the fft of the data and plot the coeffs vs frecuency
from numpy.fft import rfft, irfft

# calculate coeffs
fast_coeffs = rfft(gravity)

## the scale is gonna be divided by how often they measured, which was 1024 in .5 seconds
scaling_factor = len(fast_coeffs)/0.5
scale=len(fast_coeffs)/scaling_factor
f=linspace(0,len(fast_coeffs)/scale,len(fast_coeffs))

plt.subplot(222)
plt.plot(f,abs(fast_coeffs))
plt.ylabel('c_k Amplitude')
plt.xlim(0,120)
plt.xlabel('Frequency')

# c - clean frequencies to be in-between 20 and 80 Hz
i = 0
while i < 20 and i > 80:
    fast_coeffs[i] = 0
    i += 1

plt.subplot(223)
plt.plot(f,abs(fast_coeffs))
plt.ylabel('c_k Amplitude')
plt.xlim(0,120)
plt.xlabel('Frequency')

## d- take the inverse fft and plot the filtered signal vs. time

clean_coeffs = irfft(fast_coeffs)
plt.subplot(224)
plt.plot(time,clean_coeffs)
plt.xlabel("time")
plt.ylabel("cleaned strain values")
plt.show()

## I'm pretty sure I did the scale wrong on this one because the graphs do not change

"""
Problem 4: derivatives
Just the math at the end
"""
# x = atan(3)
# x2 = sin(x)**2
# print(9*(x2-1))
# print(3*pi/2)