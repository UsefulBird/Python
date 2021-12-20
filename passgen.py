import random 
import string
import time
letter = ["a", "b"]
contin = True
while contin == True:
    passlen = int(input("Enter the length of password: "))
    if passlen == "":
        print("You mus enter a number")
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@€£#$%^&*()"
    p = "".join(random.sample(s,passlen ))
    print(p)
    contin = False

