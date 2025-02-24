word =  input("Enter something to reverse it: ") 

newStr = ""
# for i in range(len(word) -1, -1, -1):
#     newStr += word[i]

index = len(word)-1
while(index >= 0):
    newStr += word[index]
    index -=1

print(newStr)