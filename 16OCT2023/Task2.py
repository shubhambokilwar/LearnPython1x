"""
Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
Input = 2024 / Output = Leap year
"""

# A leap year is exactly divisible by 4 except for century years (years ending with 00).
# The century year is a leap year only if it is perfectly divisible by 400.

year = int(input('Enter year to check if its leap year or not : \n'))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if year % 400 == 0 and year % 100 == 0:
    print(f'Year : {year} is a leap year')

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif year % 4==0 and year % 100 !=0:

    print(f" Year : {year} is a leap year")

#if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print(f"{year} is not a leap year")