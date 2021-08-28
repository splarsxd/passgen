from time import sleep
import os
from random import choice

# made by splars#1252

prefix = "Password Generator V4 by splars#1252"
cls = lambda: os.system("cls" if os.name == "nt" else "clear")
sleep = lambda: os.system("timeout 3 >nul" if os.name == "nt" else sleep(3))
os.system("title %s" %prefix if os.name == "nt" else "pass")
os.system("color c" if os.name == "nt" else "pass")
gen = []
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

ABC = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "!", "@", "#", "£", "¤", "$", "€", "%",
    "/", "{", "}", "[", "]", "(", ")", "=", "?", "+", "-", "^", "~", "*", "_", ".", ",",
    "§", "è", "ê", "à", "â", "û", "ù",
    "xd", "lol", "pls", "plox", "sadasd"]


def normal():
    global gen
    cls()

    try:
        print(f"{prefix}\n\n")
        length = int(input("Length of the password? \n>> "))
        if length >= 1:
            x = 0
            while x < length:
                x += 1
                gen.append(choice(abc))

            fix = "".join(gen)
            print(fix)
            print("\nPress any key to copy to clipboard")

            os.system("pause >nul")
            os.system("echo %s | clip" %fix)
            print("Copied to clipboard.")

            sleep()
            main()
        else:
            print("\nYou did not make a valid selection.")
            sleep()
            normal()
    except:
        print("\nYou did not make a valid selection.")
        sleep()
        normal()


def advanced():
    global gen
    cls()

    try:
        print(f"{prefix}\n\n")
        length = int(input("Length of the password? \n>> "))
        if length >= 1:
            x = 0
            while x < length:
                x += 1
                gen.append(choice(ABC))

            fix = "".join(gen)
            print(fix)
            print("\nPress any key to copy to clipboard")

            os.system("pause >nul")
            os.system("echo %s | clip" %fix)
            print("Copied to clipboard.")

            sleep()
            main()
        else:
            print("\nYou did not make a valid selection.")
            sleep()
            advanced()
    except:
        print("\nYou did not make a valid selection.")
        sleep()
        advanced()


def main():
    global gen
    cls()

    gen = []

    print(f"{prefix}\n\n")
    passwordtype = input("Advanced password? (e.g '! # % & ( = ? @' (Y/N) \n>> ").lower()
    if not passwordtype:
        main()

    if passwordtype == "y":
        advanced()

    elif passwordtype == "n":
        normal()

    else:
        print("\nYou did not make a valid selection.")
        sleep()
        main()
main()