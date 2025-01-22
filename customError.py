a = input("Enter a number or quit from program: ")

if(a == "quit"):
    print("You are quit from program")
elif(int(a) < 5 or int(a) > 9):
    raise ValueError("value shoud be between 5 and 9 or  quit")

