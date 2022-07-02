# Allow user to input two numbers

num1, num2 = input("Enter any two numbers:  ").split()

# convert the two numbers into integer
num1 = int(num1)
num2 = int(num2)

# sum input

sum = num1 + num2
product = num1 * num2
divide =num1/num2
subtract = num1 - num2
quotient = num1%num2

# print the result
print("{} + {} = {}".format(num1,num2, sum))
print("{} * {} = {}".format(num1,num2, product))
print("{} / {} = {}".format(num1,num2, divide))
print("{} - {} = {}".format(num1,num2, subtract))
print("{} % {} = {}".format(num1,num2, quotient))

