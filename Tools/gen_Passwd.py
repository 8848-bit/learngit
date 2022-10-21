#coding=utf-8

# Generate password whcih is tough to break for hackers.

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

Use_for = lower_case + upper_case + number + symbols
length_for_passwd = 8

password = "".join(random.sample(Use_for, length_for_passwd))
print("your generated password is: " + password)