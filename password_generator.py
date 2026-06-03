import random
import string

print("=== Password Generator ===")

length = int(input("Enter password length: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_characters = lower + upper + digits + symbols

password = ''.join(random.choice(all_characters)
                   for i in range(length))

print("\nStrong Password:")
print(password)