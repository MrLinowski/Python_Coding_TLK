#-----------------------------------------------------------------------------
# Name:        Even and Odd number checker (basics.py)
# Purpose:     To provide a sample program about the basics of Python
#
# Author:      Mr. Linowski
# Created:     14-Aug-2018
# Updated:     28-Sep-2018
#-----------------------------------------------------------------------------








# Ask the user to enter a number
number = int(input("Enter a number: "))

# Use conditional statements to check if the number is even or odd

# if the number divided by 2 has a 0 remainder then print the number is even
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
