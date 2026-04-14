text = input("Enter string: ")

rev = "".join(reversed(text))

if text == rev:
    print("Palindrome string")
else:
    print("Not a palindrome")