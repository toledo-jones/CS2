# !/usr/bin/env python3
# coding: utf-8
"""
Name: Cody Bogausch
Description:  Write a program that takes the radius of a sphere (a floating-point number) 
as input and outputs the sphere's diameter, circumference, surface area, and volume.
"""
from math import pi


def print_sphere_information(radius: float, units=""):
    """ Call this function to print to the console a sphere's
     diameter,
     circumference,
     surface area,
     volume 
     to the console. """

    print(f"Sphere Information for Radius: {radius} {units}")
    print(f"Volume : {get_volume(radius)} {units}")
    print(f"Surface Area : {get_surface_area(radius)} {units}")
    print(f"Diameter : {get_diameter(radius)} {units}")
    print(f"Circumference : {get_circumference(radius)} {units}")


def get_circumference(radius: float):
    """ Returns circumference as a float """
    return 2.0 * pi * radius


def get_surface_area(radius: float):
    """ Returns surface area as a float """
    return 4.0 * pi * radius ** 2


def get_diameter(radius: float):
    """ Returns diameter as a float """
    return radius * 2.0


def get_volume(radius: float):
    """ Returns volume as a float """
    return (4 / 3) * pi * radius ** 3


def main():
    """ Entry point """
    print("Sphere Calculator v 1.00")
    try:
        radius = float(input("Enter a radius: "))
        units = input("Enter the units of the radius: ")
        print_sphere_information(radius, units)

    # Handle bad input by restarting 
    except Exception as e:
        # Show error
        print(f"Error: {e}")
        print("Rebooting...")

        # Recurse 
        main()


# If this script is executed run as main
if __name__ == '__main__':
    main()
