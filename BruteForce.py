import random
from getpass import getpass
import string

try:
    print("""\x1b[1;31m
▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓▓█████      █████▒▒█████   ██▀███   ▄████▄  ▓█████ 
▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀    ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ 
▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███      ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███   
▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄    ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ 
░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒   ░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒
░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░    ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░
▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░    ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░
░    ░   ░░   ░  ░░░ ░ ░   ░         ░       ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░   
░         ░        ░                 ░  ░              ░ ░     ░     ░ ░         ░  ░
    ░                                                               ░               
\x1b[0;31m#################################################################
                           \x1b[0;34mBy x04000
                    \x1b[0;33mGithub: github.com/x04000
                          \x1b[0;32mBase: Python
                          \x1b[0;36mVersion: 1.0
\x1b[0;31m#################################################################
\x1b[1;34m
    """)

    option = str(input("Do you want include all chars? [Y/n] "))
    print("")

    if option == "Y":
        chars = string.printable
        chars_list = list(chars)

    else:
        o1=0
        o2=0
        o3=0
        option = str(input("Do you want include lowercase? [Y/n] "))
        if option == "Y":
            o1 = 2
        option = str(input("Do you want include uppercase? [Y/n] "))
        if option == "Y":
            o2 = 3
        option = str(input("Do you want include numbers? [Y/n] "))
        if option == "Y":
            o3 = 4
        o4 = o1+o2+o3
        if o4 == 2:
            chars = "abcdefghijklmnopqrstuvwxyz"
        if o4 == 3:
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if o4 == 4:
            chars = "0123456789"
        if o4 == 5:
            chars = "abcdefghijqlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if o4 == 6:
            chars = "abcdefghijqlmnopqrstuvwxyz0123456789"
        if o4 == 7:
            chars = "abcdefghijqlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        chars_list = list(chars)

    password = getpass("Password: ")

    num = 0
    guess_password = ""

    while(guess_password != password):
        guess_password = random.choices(chars_list, k=len(password))

        print("Attemp: "+str(num)+" | Checking "+str(guess_password))

        if(guess_password == list(password)):
            print("\x1b[1;36m")
            print("Your password is: "+"".join(guess_password))
            print("Total attemps: "+str(num))
            print("\x1b[1;34m")
            break

        num = num + 1
except:
    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt\x1b[1;34m")