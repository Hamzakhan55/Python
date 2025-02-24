num = int(input("Enter a number to find factorial: "))


if num == 0 or num == 1:
    print(f"The factorial of {num} is 1")
elif num > 1:
    new_number = 1
    for i in range(num, 0, -1):
        new_number *= i
    print(f"The factorial of {num} is {new_number}")
    