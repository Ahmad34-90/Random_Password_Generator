# Random Password Generator
Description:
This is a simple **Python-based password generator** that creates secure random passwords using a combination of:
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

The generated password length is customizable (default: 15 characters).
Features:
- Generates strong random passwords
- Includes uppercase, lowercase, numbers, and special characters
- Customizable password length
- Simple and easy-to-use Python script
How It Works:
1. The script defines the desired password length (default: `15`).
2. It creates a pool of characters from:
   - `string.ascii_letters`
   - `string.digits`
   - `string.punctuation`
   - `string.ascii_uppercase` *(already included in ascii_letters, but kept here for redundancy)*
3. It randomly selects characters from the pool to create a password.
4. Prints the generated password.
Code Example:

import random
import string

pass_len = 15
charValues = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("Your random password is: ", password)
