# Kaiden Rivera
# 09/30/26
# P3HW1
# This program takes a number grade and determines average and displays letter grade for the average.

# (P.S. I added the format I saw in the canvas instructions)

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
mod_sum = sum(grades)
avg = mod_sum / len(grades)

# determine letter grade for average
print()
print('-' * 12, 'Results', '-' * 12)

print(f'{'Lowest Grade:':20s} {low:.1f}')
print(f'{'Highest Grade:':20s} {high:.1f}')
print(f'{'Sum of Grades:':20s} {mod_sum:.1f}')
print(f'{'Average:':20s} {avg:.2f}')

print('-' * 40)

if avg >= 90:
    print('Your grade is: A')
else:
    if avg >= 80 and avg <= 89:
         print('Your grade is: B')
    else:
        if avg >= 70 and avg <= 79:
            print('Your grade is: C')
        else:
            if avg >= 60 and avg <= 69:
                print('Your grade is: D')
            else:
                print('Your grade is: F') # TO DO: finish this





