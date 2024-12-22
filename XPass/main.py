import time
import secrets
import string
import re
from colorama import Fore, Style
import random
import os
import bcrypt
import base64

def generate_random_name(length):
    letters = string.ascii_lowercase
    rname = ''.join(random.choice(letters) for i in range(length))
    return rname

def xpass():
    checkinput = input(Fore.MAGENTA + "----------------------------------\nCheck your password for data breaches: \n->" + Style.RESET_ALL)

    if not os.path.exists('py.txt'):
        bpath = '_internal'
    else :
        bpath = 'XPass'
    
    with open(bpath + '/breach.txt', 'r') as f:
        if any(line.startswith(checkinput) for line in f):
            print(Fore.GREEN + checkinput + Fore.MAGENTA + " was found in our database. We recommend changing it." + Style.RESET_ALL)
        else:
            check_pass = re.compile(r'''(
                    ^.*(?=.{10,})           
                    (?=.*\d)                
                    (?=.*[a-z])             
                    (?=.*[A-Z])             
                    (?=.*[@#$%^&+=!]).*$    
                    )''', re.VERBOSE)

            status = Fore.GREEN + "strong" if check_pass.search(checkinput) else Fore.RED + "weak"
            print(Fore.GREEN + checkinput + Fore.MAGENTA + " was not found in our database, the password is " + status + Style.RESET_ALL)

    input("->")
    menu()

def generator():
    print(Fore.MAGENTA + "_______________________________________________\nXPass Generator " + version + "\n_______________________________________________" + Style.RESET_ALL)
    pwd_length = int(input(Fore.MAGENTA + 'How many chars would you like to be in your password?\n' + Style.RESET_ALL))
    time.sleep(2)
    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(secrets.choice(alphabet) for _ in range(pwd_length))

    print(Fore.LIGHTGREEN_EX + "Generated password is : " + pwd + Style.RESET_ALL)
    input("Press enter to proceed...")
    menu()

def keychain():
    '''
    print("Welcome to XPass keychain [beta]")
    choice = input("Menu:\n[1] - Add a new password\n[2] - View your passwords\n[3] - Exit to the XPass\n-> ")
    
    if choice == '1':
        userinput = input("Enter a website for the password that you would like to add: ")
        passinput = input("Enter password that will be saved and attached to the last input: ")
        hashed_password = bcrypt.hashpw(passinput.encode('utf-8'), bcrypt.gensalt())

        with open('b.txt', 'a') as f:
            f.write(f'{userinput}:{hashed_password.decode()}\n')
        
        keychain()
    elif choice == '2':
        with open('b.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                username = parts[0]
                hashed_password = parts[1]
                print(f"Website: {username}, password: {hashed_password}")  # Display hashed password
                input("Press any key to proceed")
                keychain()
    elif choice == '3':
        menu()
    else:
        print("Invalid choice. Please try again.")
        keychain()
    '''
    print("Work in progress...")
    menu()

def check():
    if not os.path.exists('pass.txt'):
        apppass = input("pass.txt not found\nEnter a password that will be needed every time you open the app(for security): ")
        hashed_apppass = bcrypt.hashpw(apppass.encode('utf-8'), bcrypt.gensalt())
        with open('pass.txt', 'w') as f:
            f.write(hashed_apppass.decode())
        print("Operation completed.")

    with open('pass.txt', 'r') as f:
        hashed_apppass = f.read().strip()
        inputpass = input("Enter password to access the app: ")
        if bcrypt.checkpw(inputpass.encode('utf-8'), hashed_apppass.encode('utf-8')):
            menu()
        else:
            exit('Access denied')

def menu():
    asciitext = " _     _  _____  _______ _______ _______\n  \___/  |_____] |_____| |______ |______\n _/   \_ |       |     | ______| ______|"
    print(Fore.MAGENTA + asciitext + Style.RESET_ALL)
    print(Fore.MAGENTA + "version " + version + Style.RESET_ALL)
    gen = input(Fore.MAGENTA + '_________________________\n|                       |\n|Select an option       |\n|[1] - XPass            |\n|[2] - XPass Generator  |\n|[3] - XPass Keychain   |\n|[4] - Exit             |\n|_______________________|\n-> ' + Style.RESET_ALL)
    
    if gen == '1':
        xpass()
    elif gen == '2':
        generator()
    elif gen == '3':
        keychain()
    elif gen == '4':
        exit()
    else:
        print('Input is invalid')
        menu()



version = "1.3"

check()
menu()