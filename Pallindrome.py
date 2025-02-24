word = input("Enter a word to check pallindrome: ")

new_word = word.lower()
newStr = ""
index = len(new_word)-1
while index >= 0:
    newStr += new_word[index]
    index -= 1
if newStr == new_word:
    print("the word is pallindrome")
else:
    print("not pallindrome")