# Kaiden Rivera
# 10/1/26
# P3LAB
# This program allows user to enter money (float) value with two places after the decimal. The program should then do the following: Calculate efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money.

# Variables
user_money = float(input("Enter the amount of money as a float: "))
user_money = int(round(user_money * 100)) # Takes the integer type of the rounded version of the user's money times 10. If it were 12.34, the rounded int version would be 1234.

# Calculations of Dollars, Quarters, Dimes, Nickels, and Cents.
dollars = user_money // 100 # Divides the user money by 100, as it will take the dollar digits (anything 100 and above; 200, 300, 400...)
user_money = user_money - (dollars * 100) # Removes those dollar digits from the integer. If it was 1234, it would become 34.

quarters = user_money // 25
user_money = user_money - (quarters * 25) # 34 becomes 9. Because it divided 1 time, there is one quarter.

dimes = user_money // 10
user_money = user_money - (dimes * 10) # 9 is still 9, it doesn't remove for a dime, as floor division only divides by a number its able to. 0 Dimes.

nickels = user_money // 5
user_money = user_money - (nickels * 5) # 9 becomes 4, and because it divided one time, there is 1 nickel.

pennies = user_money // 1
user_money = user_money - (pennies * 1) # 4 becomes the remaining 4 as pennies.

# Display
if dollars > 0:
    if dollars == 1: # If dollars is more than 1 and is exactly one, it will display Dollar. If not, it will just display Dollars. If both are false, it will not display.
        print(f"{dollars} Dollar")
    else:
        print(f"{dollars} Dollars")

if quarters > 0:
    if quarters == 1:
        print(f"{quarters} Quarter")
    else:
        print(f"{quarters} Quarters")

if dimes > 0:
    if dimes == 1:
        print(f"{dimes} Dime")
    else:
        print(f"{dimes} Dimes")

if nickels > 0:
    if nickels == 1:
        print(f"{nickels} Nickel")
    else:
        print(f"{nickels} Nickels")

if pennies > 0:
    if pennies == 1:
        print(f"{pennies} Penny")
    else:
        print(f"{pennies} Pennies")
