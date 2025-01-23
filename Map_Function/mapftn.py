def cube(x):
    return x*x*x

l = [1,3,5,6,7]
newl = list(map(cube,l))
print(newl)

# Output
# [1, 27, 125, 216, 343]