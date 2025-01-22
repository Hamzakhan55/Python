# Multiplication Table 

a = int(input("Enter a number: "))
print(f"Multiplication Table of {a} is :")

for i in range(1,11):
    print(f"{a} x {i} = {a*i}")