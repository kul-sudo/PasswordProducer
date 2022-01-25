from string import ascii_lowercase, ascii_uppercase, digits
from random import choice
from os import path, getlogin, mkdir
from time import sleep

# Save toggle
save = input('Do you want to save your password to Documents\Generation in a text file? (Y/N) ').lower()
while save[0] != 'y' and save[0] != 'n':
    save = input("You can only use 'Y' or 'N' ")
if save[0] == 'y':
    save = True
else:
    save = False

while True:
    if save == True:
        if not path.exists(f'C:\\Users\\{getlogin()}\\Documents\\Generation'):
            mkdir(f'C:\\Users\\{getlogin()}\\Documents\\Generation')

    # Preparing
    password = ''
    yn = 'y', 'n'

    # Log
    if save == True:
        log_type = input("Type 'Over' to overwrite your saved password in a file; type 'Append' to append your saved passwords into the file ").lower()
        while log_type[0] != 'a' and log_type[0] != 'o' and log_type != 'w':
            log_type = input("You can only use 'Over' or 'Append' ").lower()
        if log_type[0] == 'o' or log_type == 'w':
            log_mode = 'w'
        else:
            log_mode = 'a+'

    # Password resource
    digitsp = input('Do you want your password to contain digits? (Y/N) ').lower()
    while digitsp not in yn:
        digitsp = input('Do you want your password to contain digits? (Y/N) ').lower()
    lowers = input('Do you want your password to contain lowercase letters? (Y/N) ').lower()
    while lowers not in yn:
        lowers = input('Do you want your password to contain digits? (Y/N) ').lower()
    uppers = input('Do you want your password to contain uppercase letters? (Y/N) ').lower()
    while uppers not in yn:
        uppers = input('Do you want your password to contain digits? (Y/N) ').lower()
    if digitsp[0] == 'y':
        digitsp = digits
    else:
        digitsp = ''
    if lowers[0] == 'y':
        lowers = ascii_lowercase
    else:
        lowers = ''
    if uppers[0] == 'y':
        uppers = ascii_uppercase
    else:
        uppers = ''
    
    if digitsp == '' and lowers == '' and uppers == '':
        print('You have nothing to get a random password from! Try again')
        sleep(1)
        continue

    # Length
    length_error = True
    while length_error:
        try:
            length = int(input('How many characters do you want your password to contain? '))
            length_error = False
        except:
            pass

    # Generating
    for _ in range(length):
        password += choice(digitsp + uppers + lowers)
    if save == True:
        with open(f'C:\\Users\\{getlogin()}\\Documents\\Generation\\strong.txt', log_mode) as slist_file:
            slist_file.write(f'{password}\n')
    else:
        print(password)