# |Imports|
import random
import string

print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ ")
print("▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
print("▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ")
print("▐░▌          ▐░▌       ▐░▌▐░▌          ")
print("▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▄▄▄▄▄▄▄▄ ")
print("▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌▐░░░░░░░░▌")
print(" ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌ ▀▀▀▀▀▀█░▌")
print("          ▐░▌▐░▌          ▐░▌       ▐░▌")
print(" ▄▄▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄█░▌")
print("▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌")
print(" ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀ ")


while True:
    # |Strings|
    strength = input("Choose the strength:")
    num = int(strength) + 1
    string.gen = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890=´ú)¨ů§,.-|_:?"!%*><$ß¤×÷%ˇ;°'

    # |Generation|
    for a in range(1, num):
        for b in range(a, num):
            print(random.choice(string.gen), end='')

    print("\n")
