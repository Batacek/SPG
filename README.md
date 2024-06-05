# SPG
This Python script is designed to generate strong passwords. If you're looking for something a bit weaker, go for level 2 or 3. If you want something really secure, aim for level 4 or higher. I'd also recommend testing the password on <a href="https://www.passwordmonster.com/">this site</a>.
<br>
# Code
```py
# |Imports|
import random
import string

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
```
