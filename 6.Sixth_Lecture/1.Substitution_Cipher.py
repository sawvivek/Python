# String
# h="Hello World"

# print(h[0]) # H
# print(h[1]) # e

# print(len(h)) # 11

# print(h.upper()) # HELLO WORLD
# print(h.lower()) # hello world

# print(h.replace("o","0")) # Hell0 W0rld
# print(h[0:5]) # Hello
# print(h[6:11]) # World

# Substitution Cipher

import string

dict={}

for i in range(26):
    dict[string.ascii_letters[i]]=string.ascii_letters[(i+3)%26]
print(dict)
