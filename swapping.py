a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))


print(f"Before Swapping  a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b

print(f"After Swapping  a = {a}, b = {b}")


# Swapping two numbers without using temp variable

# Enter the value of a: 10
# Enter the value of b: 8
# Before Swapping  a = 10, b = 8
# After Swapping  a = 8, b = 10
