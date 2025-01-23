def filter_function(a):
    return a > 10


l = [2,6,28,92,39,1,9]

newl = list(filter(filter_function, l))
print(newl)

#output
# [28, 92, 39]