# Kaiden Rivera
# 09/24/26
# P2HW1
# Program that uses the user input for budget, travel destination, amount on gas spent, accomodations, food, expenses, and displaying those results based on subtracting those expenses from the budget.

print("This program calculates and displays travel expenses") # Lets the user know what this program was made to do.
print()
budget = int(input("Enter budget: ")) # User inputs their budget, and budget becomes the variable that represents it.
print()
travel_destination = str(input("Enter your travel destination: ")) # travel_destination represents the string that the user inputs. print(travel_destination) only outputs, for example, "Orlando", but if I were to put print("Location: ", travel_destination), it shows that it is the destination they will be traveling to in the terminal output.
print() 
gas_money = int(input("How much do you think you will spend on gas? ")) # gas_money is the estimated amount spent on the drive from current destination and travel destination, represented by this variable.
print()
accomodation_money = int(input("Approximately, how much will you need for accomodation/hotel? ")) # accomodation_money represents the amount of money spent on accomodations inputted by the user.
print()
food_money = int(input("Last, how much do you need for food? ")) # food_money becomes the variable that represents the amount of food spent by the user.

expenses = gas_money + accomodation_money + food_money # Adds up all expenses into one variable. For example, 10 + 12 + 8 = 30.

remaining_balance = budget - expenses # Subtracts the expenses from the starting budget.

print() # Spacing
print(('-' * 10) + 'Travel Expenses' + ('-' * 10)) # Edited P2HW1 /////// Combines 10 dashes with Travel Expenses, then another 10 dashes.

print(f"{"Location:":20s} {travel_destination}") # Edited P2HW1 /////// Spaces out 20 times in an f string.

print(f"{"Initial Budget:":20s} ${budget}") # Edited P2HW1 ///////

print(f"{"Fuel:":20s} ${gas_money}") # Edited P2HW1 ///////

print(f"{"Accomodation:":20s} ${accomodation_money}") # Edited P2HW1 ///////

print(f"{"Food:":20s} ${food_money}") # Edited P2HW1 ///////

print('-' * 35)
print() # Spacing

print(f"{"Remaining Balance:":20s} ${remaining_balance}") # Edited P2HW1 ///////
