#for i in range(11):
 #   print(i + 1)


#def print_hell0_word(W):
 #   print("Hello Shubham")

numbers=[1,2,3,4,4,5,5,55,5]

def grether_than_10(num):
    return num > 2

op = filter(grether_than_10,numbers)
print(op)
op_list = list(op)
print(op_list)
