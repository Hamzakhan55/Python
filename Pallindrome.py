
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


# number = int(input("Enter a string to check pallindrome : "))

# new_number = 0
# index = len(number) - 1
# while number >= 0:
#     new_number += number[index]
#     number -= 1
# if number == new_number:
#     print(f"Your number {number} is Pallindrome")
# else:
#     print(f"Your number {number} is not pallindrome")
