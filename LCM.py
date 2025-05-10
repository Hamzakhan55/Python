num_1 = int(input("Enter first Number: "))
num_2 = int(input("Enter second Number: "))


num_3 = num_1 * num_2


GCD_1 = [i for i in range(2, num_1+1)
         if num_1 % i == 0]


GCD_2 = [i for i in range(2, num_2+1)
         if num_2 % i == 0]

common_item = (list(set(GCD_1) & set(GCD_2)))

max_number = max(common_item)

LCM = num_3 // max_number

print(f"LCM of {num_1} and {num_2} is {LCM}")
