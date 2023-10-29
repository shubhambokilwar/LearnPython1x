#Area of circle
r=int(input('Enter radius:\n'))
print(f'Area of circle is:\n {3.14*(r**2)}')

#Square and Cube of number
r=int(input('Enter number:\n'))
print(f'Square of number is: {r**2}\n Cube of number is: {r**3}')

#Ternary operator to find maximum of three
first=int(input('Enter first number\n'))
second=int(input('Enter second number\n'))
third=int(input('Enter third number\n'))
print('First number is greatest')if(first>=second and first>=third) else print('Second is greatest') if(second>=third) else print('Third is greatest')