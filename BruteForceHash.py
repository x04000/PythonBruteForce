import random
from getpass import getpass
import string
import hashlib

o4 = 0

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
try:
    numc = int(input("Number of characters: "))
    option = input("Do you want include all chars? [y/N] ").lower()
except TypeError:
    print("Invalid values. Exit 1.")
    exit(1)

char_list = ""

if option == "y":
    chars_list = list(string.printable)
else:
    options = (string.ascii_lowercase, string.ascii_uppercase, string.digits)
    print("""
Choose the character sets you want to use. Separate each index by commas (","). For example: 1,3
1) Lowercase
2) Uppercase
3) Digits
          """)
    chosen = input("-> ").split(",")
    for i in chosen:
        try:
            char_list += options[int(i)-1]
        except TypeError:
            print("Invalid value. Terminating program...")
            exit(1)

password = getpass("Hash: ")

num = 0
guess_password = ""
try:
    while(guess_password != password):
        guess_password = "".join(random.choice(char_list) for _ in range(numc))

        H = hashlib.md5(str(guess_password).encode('utf-8'))

        m = hashlib.md5()
        line = H.hexdigest()
        m.update(str(line).encode('utf-8'))
        word_hash = m.hexdigest()

        print("Attemp: "+str(num)+" | Checking "+str(guess_password)+" | Hash: "+word_hash)

        if(word_hash == str(password)):
            print("\x1b[1;36m")
            print("The password is: "+"".join(guess_password))
            print("Total attemps: "+str(num))
            print("\x1b[1;34m")
            break

        num = num + 1
except KeyboardInterrupt:
    print("Finishing program...")