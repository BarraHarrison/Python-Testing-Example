import math

def square(number):
    return number * number

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def surface_area_of_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)

def surface_area_of_sphere(radius):
    return 4 * math.pi * radius * radius

def volume_of_cube(side):
    return side ** 3

def volume_of_cone(radius, height):
    return (1/3) * math.pi * radius * radius * height

def volume_of_sphere(radius):
    return (4/3) * math.pi * radius ** 3