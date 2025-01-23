# Function to check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

# Input
text = input("Enter a string to check if it's a palindrome: ")

# Output
if is_palindrome(text):
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
