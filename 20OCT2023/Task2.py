#Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
#n = 12345
#sum = 15
#n = 123
#sum = 6
# Function to get sum of digits
def getSum(number):
    add = 0
    while number != 0:
        add = add + (number % 10)
        number = number // 10

    return add


n = int(input("Enter a number to compute sum of digits in number: \n"))
print("Sum of digits of", n, "is :", getSum(n))