"""
this program will take two numbers as input and print the greater number
"""



print("what is your first number")
num1 = int(input())
print("what is your second number")
num2 = int(input())


print("The greater number is :")
if num1 > num2 :
    print(num1)
elif num2 > num1 :
    print(num2)