# 1. Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than, or equal to the second number.

number1 = int(input("Enter 1st number: \n"))
number2 = int(input("Enter 2nd number: \n"))

if number1 > number2:
    print("number1 is greater than number2")
elif number1 < number2:
    print("number1 is less than number2")
else:
    print("number1 & number2 is equal")


print("-----------------------------------")

# 2. Use the ternary operator to find the maximum of three numbers entered by the user.

a = int(input("Enter first number : \n"))
b=  int(input("Enter second number : \n"))
c=  int(input("Enter third number : \n"))

max_num = a if(a>b and a>c) else(b if b>c else c)
print("The maximum of 3 numbers is : ", max_num)

print("-----------------------------------")

# 3. Develop a Python script that calculates the square and cube of a given number.

number= int(input("Enter the number for calculating its square: \n"))

print("The square of number is : ", number**2)
print("The cube of number is : ",number**3)

# 4. Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)

from math import pi

radius_value = float(input("enter radius of circle value : \n "))
print("Area of circle is :",pi * radius_value * radius_value)