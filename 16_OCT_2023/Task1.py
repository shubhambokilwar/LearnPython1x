# Grade Calculator:
# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:


# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# If, elif, else

score = int(input('Enter the number to check grade scale :\n'))
if score in range(90, 101):
    print('The grade scale for this is A:\n', score)
elif score in range(80,90):
    print('The grade scale for this is B:\n', score)
elif score in range(70,80):
    print('The grade scale for this is C:\n', score)
elif score in range(60,70):
    print('The grade scale for this is D:\n', score)
elif score in range(0,60):
    print('The grade scale for this is F:\n', score)
else:
    print('The given number is out of range', score)


