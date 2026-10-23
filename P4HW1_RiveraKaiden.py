# Kaiden Rivera
# 10/22/26
# P4HW1
# This program asks input for number of scores they would like to enter and creates a loop to collect the number of scores the user wants to enter.
score_list = []

'''
User inputs amount of scores
User enters each score
if score is >= 0 and <= 100, it will append to the list
if score is < 0 or > 100, it will state invalid score, and ask user to enter the score again.
prints out the results in format (lowest score, modified list, scores average and letter grade.)
'''

user_input = int(input("How many scores would you like to enter?: "))

for i in range(1, user_input + 1):
    num_input = float(input(f"Enter score #{i}: "))

    if num_input >= 0 and num_input <= 100:
     score_list.append(num_input)
    else:
       while num_input < 0 or num_input > 100:  
        print() # Extra Line 
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        num_input = float(input(f"Enter score #{i} again: "))

        if num_input >= 0 and num_input <= 100:
          score_list.append(num_input)
       
# Loop Broken:
average = sum(score_list) / len(score_list)
print() # Extra Line
print('-' * 20 + "Results" + '-' * 20)
print(f"Lowest Score{":":10s} {min(score_list)}")
print(f"Modified List{":":10s} {score_list}")
print(f"Scores Average{":":10s} {average:.2f}")

letter_grade = ""

if average >= 50 and average <= 59:
  letter_grade = "F"
else:
  if average >= 60 and average <= 69:
    letter_grade = "D"
  else:
    if average >= 70 and average <= 79:
      letter_grade = "C"
    else:
      if average >= 80 and average <= 89:
        letter_grade = "B"
      else:
        if average >= 90 and average <= 100:
          letter_grade = "A"

print(f"Grade{":":10s} {letter_grade}")
print('-' * 47)