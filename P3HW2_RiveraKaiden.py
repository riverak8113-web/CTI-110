# Kaiden Rivera
# 09/30/26
# P3HW2
# This program prompts user input of employee name, # hours worked the week, and pay rate, then calculates if time was overworked, overtime pay, regular and gross pay.

# Request employee info
name = str(input("Enter employee name: "))
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))

# Evaluate overtime pay
if hours > 40:
    # Calculate Overtime
    overtime_hours = hours - 40
    # Calculate overtime pay
    overtime_pay = overtime_hours * (rate * 1.5) # What this does is it calculates overtime pay using the overtime_hours specifically times the rate, which the rate is multiplied by 1.5 due to overtime.
    # Calculating salary for regular hours
    regular_pay = 40 * rate
    # Calculate total pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    gross_pay = hours * rate
    regular_pay = gross_pay

# Display results
print('-' * 40)
print("Employee Name: ", name)
print(f"{'Hours Worked:':<15}{'Pay Rate':<12}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<15}")
print('-' * 75)
print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}') # Pseudocode: Display hours:15s, rate:12s, overtime_pay:15s, regular_pay:15s, gross_pay:15s | this code simplifies how it looks. What it does is it displays to the user the hours, rate, overtime pay, regular pay and gross pay. However, all of them use 15 spaces (15s) with the exception of rate (12s)