import sys

num = int(input("Enter a number: "))
is_prime = False
if num == 2:
    print("Prime")
    sys.exit()
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
    else:
        is_prime = True

if is_prime == True:
    print("prime")
elif is_prime == False:
    print("Not prime")
