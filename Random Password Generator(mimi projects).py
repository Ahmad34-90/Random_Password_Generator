import random
import string


pass_len= 15
charValues = string.ascii_letters+string.digits+  string.punctuation+ string.ascii_uppercase
print("-------------Welcome to PAssword Generator---------------")
#password = "".join([random.choice(charValues) for i in range(pass_len)])
password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("Your random password is: ", password)
