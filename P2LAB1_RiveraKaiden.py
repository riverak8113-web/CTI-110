# Kaiden Rivera
# 09/21/26
# P2LAB1
# The following program calculates the area of a circle, diameter, and the circumference.

# Import math module to use the constant, math.pi
import math

# Get radius from user
radius = float(input("What is the radius of the circle?: "))
print()

# Get diameter from user
diameter = 2 * radius

# Display diameter with 1 decimal point
print(f"The diameter of the circle is {diameter:.1f}\n")

# Calculate circumference
circumference = 2 * math.pi * radius

# Display circumference with 2 decimal places
print(f"The circumference of the circle is {circumference:.2f}\n") # Pseudocode format: Display "The circumference of the circle is, ", circumference:.2f  | this is code that ordinary people can comprehend.

# Calculate area
area = math.pi * radius**2

# Display area with 3 decimal places
print(f"The area of the circle is {area: .3f}")

