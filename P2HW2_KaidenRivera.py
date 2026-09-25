# Kaiden Rivera
# 09/24/26
# P2HW2
# Program that uses the user input for test grades for Modules 1-6, creates a list, and uses the list to display lowest, highest, sum, and average of grades.

# Inputs
module_1 = float(input("Enter grade for Module 1: ")) # Asks for input for each module (in floats / ex. 2.43; decimals)
module_2 = float(input("Enter grade for Module 2: "))
module_3 = float(input("Enter grade for Module 3: "))
module_4 = float(input("Enter grade for Module 4: "))
module_5 = float(input("Enter grade for Module 5: "))
module_6 = float(input("Enter grade for Module 6: "))
print() # Spacing

# Creating a List
module_list = [module_1, module_2, module_3, module_4, module_5, module_6] # List of all variable inputs

# Calculations
lowest_grade = min(module_list) # Takes the minimum of all the values inside the module_list /// Pseudocode: Set lowest_grade to minimum(module_list)
highest_grade = max(module_list) # Takes the maximum of all the values inside the module_list
grades_sum = sum(module_list) # Takes the sum of all the values inside the module_list
grade_average = grades_sum / len(module_list) # Takes the grades_sum variable value and divides it by the amount of variables inside of the list

# Display
print(('-' * 12) + "Results" + ('-' * 12)) # Prints 12 dashes, then prints Results in the middle along with 12 more dashes.
print(f"{"Lowest Grade:":15s} {lowest_grade: .1f}") # Prints the string and then spaces out 15 times then prints the variable with 1 decimal float point precision.
print(f"{"Highest Grade:":15s} {highest_grade: .1f}")
print(f"{"Sum of Grades:":15s} {grades_sum: .1f}")
print(f"{"Average:":15s} {grade_average: .2f}") # Prints the variable with 2 decimal float point precision. /// Pseudocode: Join ("Average: ":15spaces) + (grade_average:2decimalplaces)
print('-' * 40) # Prints 40 dashes.

