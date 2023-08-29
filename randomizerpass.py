# Code1

# import random

# lower = "abcdefghijklmopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "[]{}()*;/,._-"
 
# print ("Your password: ")

# all = lower + upper + numbers + symbols
# length = 16
# password = "".join(random.sample(all,length))

# print (password)

# Code2

import random

print ("Your Password: ")

chars = 'abcdefghijklmnopqrstuvwxyz0123456789{}()!@#$%^&*?:;""/'

password = ""
for x in range (16):
    password += random.choice(chars)

print (password)
