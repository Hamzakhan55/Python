# find factorial of a number


num = int(input("Enter a number: "))
result = 1
for i in range(2, num+1):
    result = result*i
    
print(f"The factorial of {num} is {result}")
