word = input("Enter a word that count vowels: ")
vowels = 'aeiou'

new_word = word.lower()
count = 0

for i in new_word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1

print(count)


