# Write a password generator in Python

import random
import string
import sys


try:
    size = int(sys.argv[1])
except Exception:
    size = 8

char_list = string.ascii_letters + string.digits + string.punctuation
print("".join(random.choices(char_list, k=size)))
