a = input("Enter a number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{a} x {i} = {int(a)*i}")
except Exception as e:
    print(e)
print("Some line of code")
print("Good By")