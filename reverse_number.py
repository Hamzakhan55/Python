
num = input("Enter a number to reverse it: ")

reverse = 0
while num > 0:
    temp = num % 10
    num = int(num/10)
    reverse = (reverse * 10) + temp


print(reverse)


# print(622 % 10) 2,2,6
# print(int(622 / 10)) 622,62,6
# revese 2,2,6


# print(num[::-1])
