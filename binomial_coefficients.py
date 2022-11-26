###############################
# in-class assignment day 4
# calculate binomial coefficients to make pascal's triangle
###############################

from math import factorial

## check to make sure factorial(0)works (it does)
# print(factorial(4),factorial(0))
# make bin. function
def compute_bc(n,k):
    bc = factorial(n)/(factorial(k)*factorial(n-k))
    return int(bc)

#get values to calculate binomial coeff.
top = int(input("Enter a value for n: "))
bottom = int(input("Enter a starting value for k: "))

#print(compute_bc(top,bottom))
##part b: make pascal's triangle
# for i in range(top):
#     print()
#     for j in range(i+1):
#         print(compute_bc(i,j),end=" ")

## part c: compute probability                
def compute_prob_coin(n,k):
    prob = compute_bc(n,k)/(2**n)
    return prob

print(f"The probability you will get {bottom} heads in {top} coin flips is {compute_prob_coin(top,bottom)}")
prob = 0
for i in range(bottom, top+1):
    prob += compute_bc(top,i)/(2**top)

print(f"The probability of getting {bottom} or more heads from {top} coin flips is {prob}")
