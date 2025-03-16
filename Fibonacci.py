num = int(input("Enter a number to find fibonacci series: "))

new_num = [0, 1]
for i in range(2, num):
    Last = new_num[-1]
    second_last = new_num[-2]
    next_num = Last + second_last
    new_num.append(next_num)

print(new_num)
