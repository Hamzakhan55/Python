num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))

num_1_D = [1]
num_2_D = [1]

for i in range(2, num_1+1):
    if num_1 % i == 0:
        num_1_D.append(i)


for i in range(2, num_2+1):
    if num_2 % i == 0:
        num_2_D.append(i)


print(num_1_D)
print(num_2_D)

common_items = (list(set(num_1_D) & set(num_2_D)))

print(f"Greatesr Common Divisor is : {max(common_items)} ")

# input
# Enter number 1: 100
# Enter number 2: 98

# Output
# [1, 2, 4, 5, 10, 20, 25, 50, 100]
# [1, 2, 7, 14, 49, 98]
# Greatesr Common Divisor is : 2
