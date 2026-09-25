# Kaiden Rivera
# 09/21/26
# P2LAB2
# This program creates and uses a dictionary where the key and value are pairs.

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

# Get keys from dict
cars_key = cars.keys()

print(cars_key)
print()

print(*cars, sep = ", ")
print()

# Get a car from user
car_name = input("Enter a car: ")
print()

# Get mpg for the given car
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon.\n")

# Get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}?: "))
print()

# Calculate gallons of gas needed
gallons_needed = miles_driven / car_mpg

# Display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles") # Pseudocode format: Display gallons_needed:.2f, " gallons of gas are needed to drive the ", car_name, " ", miles driven, " miles" | Another way of showing the separation and concatenations of the code.

