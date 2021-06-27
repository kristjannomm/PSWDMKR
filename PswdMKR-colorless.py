#PswdMKR colorless 2.0
#MIT License
#Copyright (c) 2021 kristjannomm
import sys
import random

print("PswdMKR 2.0")
print("github.com/kristjannomm/PSWDMKR")

print ("-------------------------------")

#Chars (short for character) defines 
#the letters and symbols that are in the password 
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!&=?-$€£(/)"

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
                print ("Here is your password -> ", password)
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
                print ("Siin on sinu parool -> ", password)
                print ("Vajutage [CTRL+C], et lahkuda")
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
                print ("Нажмите [CTRL + C], чтобы выйти")
        else:
            sys.exit()

#todo
#with password("save.txt", "w") as f:
#    f.write(password + ",")