# Kaiden Rivera
# 10/22/26
# P4HW2
# This program prompts user input of employee name, # hours worked the week, and pay rate, then calculates if time was overworked, overtime pay, regular and gross pay.

'''

'''

# Request employee info
name = str(input("Enter employee name or 'done' to finish: "))

# Create accumulator variables for overtime pay, regular pay, gross pay and employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'done':
    # Add employee count plus 1
    employee_count += 1 # employee_count = employee_count + 1
    # Ask for employee info
    hours = float(input("How many hours did " +name+ " work this week?: "))
    rate = float(input("What is " +name+ "'s hourly pay rate?: "))

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

    # Add to our accumulator totals
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay


    # Display results
    print('-' * 40)
    print("Employee Name: ", name)
    print(f"{'Hours Worked:':<15}{'Pay Rate':<12}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<15}")
    print('-' * 75)
    print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}') # Pseudocode: Display hours:15s, rate:12s, overtime_pay:15s, regular_pay:15s, gross_pay:15s | this code simplifies how it looks. What it does is it displays to the user the hours, rate, overtime pay, regular pay and gross pay. However, all of them use 15 spaces (15s) with the exception of rate (12s)

    print()
    name = str(input("Enter employee name or 'done' to finish: "))

print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular time: $", format(regularpay_total, ',.2f'))
print("Total amount paid in gross: $", format(grosspay_total, ',.2f'))