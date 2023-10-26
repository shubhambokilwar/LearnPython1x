# Factorial

number = int(input('Enter the number: '))
output = 1
for i in range(2, number + 1):
   output *= i

print(f'factorial of {number} is = {output}')
