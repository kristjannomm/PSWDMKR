#PswdMKR 2.0
#MIT License
#Copyright (c) 2021 kristjannomm
import sys
import random
from termcolor import colored, cprint

intro = colored('PswdMKR 2.0', 'cyan', attrs=['reverse',"bold" , 'blink'])
print(intro)
github = colored('github.com/kristjannomm/PSWDMKR', 'white', attrs=['reverse', 'blink'])
print(github)
print ("-------------------------------")

#Chars (short for character) defines 
#the letters and symbols that are in the password 
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!&=?-$€£(/)"

#Pick the language for the program
#Currently languages available:
#English
cprint('ENG:Choose your language [1]', 'red' ,'on_white')

#Estonian (Eesti keel)
cprint("EST:Valige oma keel [2]", "blue" ,"on_white")

#Russian (Русский язык)
cprint("RUS:Выберите свой язык [3]", "white", "on_red")

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
                print ("Here is your password -> ", password)
                cprint("Press [CTRL+C] to exit", "blue")
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
                print ("Siin on sinu parool -> ", password)
                cprint ("Vajutage [CTRL+C], et lahkuda", "blue")
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
                print ("Ваш пароль -> ", password)
                cprint ("Нажмите [CTRL + C], чтобы выйти", "blue")
        else:
            sys.exit()

#todo
#with password("save.txt", "w") as f:
#    f.write(password + ",")