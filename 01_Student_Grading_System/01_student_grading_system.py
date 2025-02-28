#-----------------------------------------------------------------------------
# Name:        Student grading system (01_student_grading_system.py)
# Purpose:     Determines a grade based on a given score
#
# Author:      Mr. Linowski
# Created:     27-Feb-2025
# Updated:     28-Feb-2025
#-----------------------------------------------------------------------------
# Ask the user to enter their score
score = int(input("Please enter your score out of 100: "))

# Determine the grade based on the score
if score >= 90:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
else:
    print("Grade: F")
