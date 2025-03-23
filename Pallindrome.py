
word = input("Enter a string to check pallindrome : ")

new_word = word.lower()
new_str = ''
index = len(new_word) - 1
while index >= 0:
    new_str += new_word[index]
    index -= 1
if new_word == new_str:
    print(f"your string {word} is pallindrome")
else:
    print(f"Your string {word} is not Pallindrome")
