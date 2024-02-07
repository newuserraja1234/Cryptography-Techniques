def leno(text):
    if text == '':
        return "You  must enter a password."
    else:
        return 1

def len8(text):
    if(len(text)<8):
        return "Password must have a Minimum of 8 character."
    else:
        return 1

def firstup(text):
    if text[0].isupper():
        return 1
    else:
        return "Password must have a capital as a first letter."

def lastlow(text):
    if text[-1].isupper():
        return "Last character must be lower case."
    else:
        return 1

def onedig(text):
    condition = False
    for letter in text:
        if letter.isdigit():
            condition = True
    if condition == False:
        return "Password must have one numeric value."
    else:
        return 1

conditions = [leno, len8, firstup, lastlow, onedig]

while(True):
    password = input("Enter a password: ")
    loe = []
    flag = 0

    for condition in conditions:
        result = condition(password)
        if result != 1:
            loe.append(result)
            flag += 1

    if flag != 0:
        for error in loe:
            print(error)
    else:
        print("Password is Fine.")
        break


    
