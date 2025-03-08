

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if (num1 > num2):
#     print(f"{num1} is greater")
# elif (num1 == num2):
#     print(f"{num1} is equal to {num2}")
# else:
#     print(f"{num2} is greater")


num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greater than {num2} and {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater than {num1} and {num3}")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is greater than {num1} and {num2}")
else:
    print("All numbers are equal")
