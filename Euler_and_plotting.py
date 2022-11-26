# """
# problem 1:
# A plastic ball is dropped from a given height and we are given 
# the drag coefficient. 
# Write a Python program that uses Euler's equations to calculate time in the air
# """

## import anything necessary
from numpy import pi, empty, sqrt
from matplotlib.pyplot import imshow, show

# ##define variables
# mass_ball = 49.5 # grams
# radius_ball = 1.36 # cm
# height = 36.7 # m
# air_density = 1.2 # kg/m^3
# g = 9.8 
# y = 36.7
# velocity = 0
# time = 0

# # define equations
# def get_acceleration():
#     a = -g - (drag_c * air_density * pi * (radius_ball**2) * (velocity**2))/ 2 * mass_ball
#     return a

# def get_velocity(acceleration):
#     v_new = velocity + acceleration * time
#     return v_new

# def get_y_value(acceleration):
#     y_new = y + velocity * time + .5 * acceleration * time**2
#     return y_new

# # the while loop where all the magic happens
# # an if-statement to determine the drag coefficient
# while y>0:
#     if velocity<10:
#         drag_c = 0.5
#     elif velocity>=10:
#         drag_c = 0.7 - 0.02 * velocity
#     # calculate values for the next step
#     a_new = get_acceleration()
#     v_new = get_velocity(a_new)
#     y_new = get_y_value(a_new)
#     # set them to be the new ones for the next calculation
#     velocity = v_new
#     y = y_new
#     time += 0.01

# # print values... hopefully
# print(f"time passed until the ball hits the ground: {time} seconds")
# ## Wait did that actually work?

"""
problem 2:
we are given an electric dipole
make a density plot of the voltage due to the electric dipole
I got most of my logic from example 3.1 on page 108
"""
# define variables
q1 = 3.5e-6
q2 = -3.5e-6
distance = 10 # between the charges, cm
k = 8.99e9 # Nm^2/C^2
side = 100 # how big is the graph? cm
spacing = 1 # spacing of points, cm
points = 100

## calculate the position of the dipole
x1 = side/2 + distance/2
y1 = side/2
x2 = side/2 - distance/2
y2 = side/2

## make an array for the voltage values
voltages = empty([points, points],float)

## calculate the values for the array
for i in range(points):
    y = spacing * i
    for j in range(points):
        x = spacing * j
        r_charge1 = sqrt((x-x1)**2 + (y-y1)**2)
        r_charge2 = sqrt((x-x2)**2 + (y-y2)**2)
        voltages[i,j] = k * (q1 / r_charge1 + q2 / r_charge2)

## plot the thing and hope for the best
imshow(voltages, origin="lower", extent=[0, side, 0, side])
show()

# """
# Problem 3:
# Given a mass spectrometer and an equation for the mass of an ion traveling 
# through the delta V and a magnetic field.

# Write a Python program that asks a user for a value of delta V and gives the mass 
# in atomic mass units (u) as the output. Use one user-defined function to 
# calculate the mass in kg and a second user-defined function to 
# convert the mass from kg to atomic mass units. 
# """
# print()
# ## define variables
# distance = .075 # m
# mag_field = .03 # T
# electron_charge = 1.6e-19 # C

# #convert kilograms to u, divide by conversion factor
# def kg_to_amu(kg):
#     u = kg / 1.661e-27
#     return u

# # calculate the mass with the value from the user
# def find_mass(delta_v):
#     mass = (distance**2 * mag_field**2 * electron_charge) / (8 * delta_v)
#     return mass 

# # get the value from the user
# delta_v = float(input("Enter the accelerating potential: "))
# mass_kg = find_mass(delta_v)
# mass_u = kg_to_amu(mass_kg)
# print(f"The mass of the ion in atomic units is {mass_u}")
# ## I assume this works? There's no values to test to make sure it works.
