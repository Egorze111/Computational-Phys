"""
Recreate figure 5.4 to show pictorally the gaussian weights
"""

from derivatives.gaussxw import gaussxwab, gaussxw
from matplotlib.pyplot import bar, show, subplot
from numpy import cos, sqrt

Na = 10
Nb = 100
a = 0
b = 1
s = 0

x1,w1 = gaussxw(Na)
x2,w2 = gaussxw(Nb)

# subplot(121)
# bar(x1,w1,width=.01)

# subplot(122)
# bar(x2,w2,width=.01)
# show()

"""
part b-- evaluate the integral
"""
def f(x):
    return (cos(sqrt(100 * x)))**2

## calculate the mapped values of x and w
xp,wp = gaussxwab(Na, a, b)
for k in range(Na):
    s += wp[k] * f(xp[k])

print(s)
