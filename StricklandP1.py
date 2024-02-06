# Strickland
# Programmer: Jameson Strickland
# Purpose: provides capability to calculate volume and surface area of a pyramid.
# Python version: 3.7.8

#to be added: GUI shape selection, area (2D) or volume (3D) selection 


# Length of the base:  a
# Height of the pyramid:  h
# Volume = (((a^2)(h))/3)
# Slant height, s  = sqrt(h^2 + (a/2)^2)  This is the Pythagorean Theorem part.
# Area of one pyramid side = s*a/2

import math

print("When prompted, please input values.")


a = float(input("Enter a value for the length of the base of the pyramid (in feet): "))

h = float(input("Enter a value for the height of the pyramid (in feet): "))

s = float(math.sqrt((h**2) + ((a/2)**2)))
    
volume = (a**2)*(h/3)

surfacearea = (((s)*(a/2))*4)

print('Base: ',a)
print('Height: ',h)
print('Volume of Pyramid: ',"%.3f" % volume)
print('Surface Area of Pyramid (without base): ',"%.3f" % surfacearea)




