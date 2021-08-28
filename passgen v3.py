from os import system
from random import choice

gen = []
prefix = "Password Generator V3 by splars#1252"
spacer = "\n"
system("color c")
system("title %s" %prefix)

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
       "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
       "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

abcadv = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
       "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
       "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
       "!", "@", "#", "£", "¤", "$", "€", "%",
       "/", "{", "}", "[", "]", "(", ")", "=", "?", "+", "-", "´", "´´", "`", "``", "^", "^^", "~", "~~", "*", "_", ".", ",",
       "µ", "§", "½", "å", "ä", "ö", "Å", "Ä", "Ö", "è", "ê", "à", "â", "û", "ù"]

print(prefix)
print(spacer)
choiceofpass = input("Advanced password? (e.g \"åäö\"  \"!\"#¤%&/()=?\"  \"@£$€{[]}\\\" (Y/N) \n>> ").lower()

# yes
if choiceofpass == "y":
    system("cls")
    print(prefix)
    print(spacer)
    
    try:
        length = int(input("Length of the password? \n>> "))
    
    except:
        system("echo.")
        system("echo Please do try a valid input next time.")
        system("ping 127.0.0.1 -n 2 >nul 2>&1")
        exit()

    x = 0

    while x < length:
        x += 1
        gen.append(choice(abcadv))

    system("echo.")
    fix = "".join(gen)
    print(fix)


    system("echo.")
    clipboard = input("Add password to clipboard? (Y/N) \n>> ").lower()

    if clipboard == "y":
        system("echo %s | clip" %fix)
        system("echo.")

        print("Copied to clipboard.")
        system("echo.")
        system("timeout 5")
        exit()
    
    else:
        system("echo.")
        system("echo null was copied to clipboard.")
        system("ping 127.0.0.1 -n 2 >nul 2>&1")
        exit()

# no
elif choiceofpass == "n":
    system("cls")
    print(prefix)
    print(spacer)

    try:
        length = int(input("Length of the password? \n>> "))
    
    except:
        system("echo.")
        system("echo Please do try a valid input next time.")
        system("ping 127.0.0.1 -n 2 >nul 2>&1")
        exit()
 
    x = 0

    while x < length:
        x += 1
        gen.append(choice(abc))

    system("echo.")
    fix = "".join(gen)
    print(fix)


    system("echo.")
    clipboard = input("Add password to clipboard? (Y/N) \n>> ").lower()

    if clipboard == "y":
        system("echo %s | clip" %fix)
        system("echo.")

        print("Copied to clipboard.")
        system("echo.")
        system("timeout 5")
        exit()

    else:
        system("echo.")
        system("echo null was copied to clipboard.")
        system("ping 127.0.0.1 -n 2 >nul 2>&1")
        exit()

else:
    system("echo.")
    system("echo Please do try a valid input next time.")
    system("ping 127.0.0.1 -n 2 >nul 2>&1")
    exit()
