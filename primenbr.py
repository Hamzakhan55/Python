import sys

num = int(input("Enter a number: "))
is_prime = True
if num == 2:
    print("Prime")
    sys.exit()
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

print("prime") if is_prime else print("Not Prime")

# if is_prime:
#     print("prime")
# else:
#     print("Not prime")
