num = int(input("Enter the number: "))

for i in range(2, num+1):
    if i * i == num:
        print(f"The square root of {num} is : {i}")
    else:
        print(f"{num} is not a perfect square")
        break
