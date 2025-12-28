import random
import string

password = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
       '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
       '@', '#', '-', '_', ';', ':', ')', '(',
       ]
password = ""
characters = string.ascii_letters + string.digits + string.punctuation
for i in range(1,100,1):
    password += random.choice(characters)


print("Generated Password:", password)
