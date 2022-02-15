import random as r
import time
normal = "abcdefghijklmnopqrstuvwxyz"


def shuffle(string):
    newstring = string
    newstring_backup = newstring
    for i in range(len(string)):
        pos = r.randint(0, len(string) -1)
        newstring = newstring_backup[:pos]
        newstring += newstring_backup[pos + 1:]
        newstring += newstring_backup[pos]
        newstring_backup = newstring
    return newstring

crypted = shuffle(normal.upper())


ask = input(": ").lower()
result = ""
for letter in ask:
    if letter == " ":
        result += " "
    else:
        change = normal.index(letter)
        result += crypted[change]
print("Encrypting...")
time.sleep(0.5)
print(result)
print("decoded = " + normal)
print("crypted = " + crypted)