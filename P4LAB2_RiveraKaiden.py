# Kaiden Rivera
# 10/22/26
# P4LAB2
# This Program asks user for input, and if the integer is >= 0, displays the multiplication table for that number from 1-12. If < 0, displays a message that the value is not accepted.

'''
Get integer from user
Determine if integer is positive or negative
If number is positive, display multiplication table
If number is negative, tell the user the program will not accept the value.
Ask the user to run again?
If yes, run program
If no, end program
'''

run_again = "yes"

while run_again != "no":
    user_num = int(input("Enter an integer: "))
    print() # Extra Line

    if user_num >= 0:
        # Display multiplication table for that value, and range (1-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values.")
    
    print() # Extra Line

    run_again = input("Would you like to run the program again?: ")

#Loop has broken. User entered "no"
print() # Extra Line
print("Exiting program...")