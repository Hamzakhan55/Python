from functools import reduce

numbers = [1,3,3,6,8,10]

def mysum(x,y):
    return x + y

sum = reduce(mysum, numbers)
print(sum)

# output
# 31


# Step by step interpret due to reduce ftn

# [1,3,3,6,8,10]
# [4,3,6,8,10]
# [7,6,8,10]
# [13,8,10]
# [21,10]
# [31]