#PswdMKR
#MIT License
#Copyright (c) 2021 kristjannomm
import sys
import random
import os
import pathlib

print("PswdMKR 2.1")
print("github.com/kristjannomm/PSWDMKR")

print ("-------------------------------")

large_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
special = "!&=?-$€£(/)"
#Chars (short for character) defines 
#the letters, numbers and symbols that are in the password
chars = large_letters + letters + numbers + special

#Pick the language for the program
#Currently languages available:
#English
print('ENG:Choose your language [1]')

#Estonian (Eesti keel)
print("EST:Valige oma keel [2]")

#Russian (Русский язык)
print("RUS:Выберите свой язык [3]")

#Asking for input
question = input("-> ")
start_over = 10
#English (1)
if question == ("1"):
    while 1:
            password_len = int(input("What length would you like your password to be -> "))
            password_count = int(input("How many passwords would you like -> "))
            for x in range(0,password_count):
                password = ""
                for x in range(0,password_len):
                    password_char = random.choice(chars)
                    password      = password + password_char
                print('\x1b[6;30;42m' + "Here is your password -> ", password + '\x1b[0m')      
            #saves the password
            with open('password.txt', 'w') as f:
                f.write(password)
            print ("Your passowrd has been saved at ->",(pathlib.Path().resolve())) 
            #end
            print ("Press [CTRL+C] to exit")
    else:
            sys.exit()

#Wrong input
else:
    print("ENG(1), EST(2), RUS(3)")
#Estonian
if question == ("2"):
    while 1:
            password_len = int(input("Kui pikk parool peab olema -> "))
            password_count = int(input("Mitu parooli on vaja -> "))
            for x in range(0,password_count):
                password = ""
                for x in range(0,password_len):
                    password_char = random.choice(chars)
                    password      = password + password_char
                print('\x1b[6;30;42m' + "Siin on sinu parool -> ", password + '\x1b[0m') 
                #saves the password
                with open('password.txt', 'w') as f:
                    f.write(password)
                print ("Su parool on salvestatud asukohta ->",(pathlib.Path().resolve())) 
                #end
                print ("Vajuta [CTRL+C], et lahkuda")
    else:
            sys.exit()

#Russian
if question == ("3"):
        while 1:
            password_len = int(input("Какой длины вы хотите, чтобы ваш пароль был -> "))
            password_count = int(input("Сколько паролей вы хотите -> "))
            for x in range(0,password_count):
                password = ""
                for x in range(0,password_len):
                    password_char = random.choice(chars)
                    password      = password + password_char
                print('\x1b[6;30;42m' + "Ваш пароль -> ", password + '\x1b[0m') 
                #saves the password
                with open('password.txt', 'w') as f:
                    f.write(password)
                print ("Your passowrd has been saved at ->",(pathlib.Path().resolve())) 
                #end
                print ("Нажмите [CTRL + C], чтобы выйти")
        else:
            sys.exit()
