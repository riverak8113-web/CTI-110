# Kaiden Rivera
# 09/9/2026
# P1HW2
# Program that uses the user input for budget, travel destination, amount on gas spent, accomodations, food, expenses, and displaying those results based on subtracting those expenses from the budget.

print("This program calculates and displays travel expenses") # Lets the user know what this program was made to do.
budget = int(input("Enter budget: ")) # User inputs their budget, and budget becomes the variable that represents it.
travel_destination = str(input("Enter your travel destination: ")) # travel_destination represents the string that the user inputs. print(travel_destination) only outputs, for example, "Orlando", but if I were to put print("Location: ", travel_destination), it shows that it is the destination they will be traveling to in the terminal output. 
gas_money = int(input("How much do you think you will spend on gas? ")) # gas_money is the estimated amount spent on the drive from current destination and travel destination, represented by this variable.
accomodation_money = int(input("Approximately, how much will you need for accomodation/hotel? ")) # accomodation_money represents the amount of money spent on accomodations inputted by the user.
food_money = int(input("Last, how much do you need for food? ")) # food_money becomes the variable that represents the amount of food spent by the user.
expenses = gas_money + accomodation_money + food_money # Adds up all expenses into one variable. For example, 10 + 12 + 8 = 30.
remaining_balance = budget - expenses # Subtracts the expenses from the starting budget.

print() # Spacing
print("----------Travel Expenses----------") # Title print
print("Location: ", travel_destination) # Location: location print
print("Initial Budget: ", budget) # Initial Budget: budget print
print() # Spacing
print("Fuel: ", gas_money) # Fuel: Gas money print
print("Accomodation: ", accomodation_money) # Accomodation: accomodation money print into the terminal
print("Food: ", food_money) # Food: Food money print
print() # Spacing
print("Remaining Balance: ", remaining_balance) # Shows the full result of all expenses - the initial budget, showing how much will remain once they make it to their destination.
