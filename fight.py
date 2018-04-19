import random
import os
import math


def collision(x1, y1, x2, y2):

    if (math.sqrt((x2 - x1)**2 + (y2 - y1)**2)) == 1:

        return True


def charactersP1():

    chars1 = ['z', 'x', 'c']
    stry = ""
    charsForPlayer1 = []
    i = len(chars1)
    while i > 0:
        w = random.randint(0, 2)
        if chars1[w] not in charsForPlayer1:
            charsForPlayer1.append(chars1[w])
            stry += chars1[w]
            i -= 1
    return charsForPlayer1


def charactersP2():

    chars2 = ['b', 'n', 'm']
    charsForPlayer2 = []
    i = len(chars2)
    while i > 0:
        w = random.randint(0, 2)
        if chars2[w] not in charsForPlayer2:
            charsForPlayer2.append(chars2[w])
            i -= 1
    return charsForPlayer2


class Variable:
    charactersP1_static = charactersP1()
    charactersP2_static = charactersP2()
    killState = False
    var_countP1 = 0
    var_countP2 = 0

def on_pressPlayer1(key):

    try: k = key.char
    except: k = key.name
    if k is Variable.charactersP1_static[Variable.var_countP1] and Variable.killState == False:  # keys interested
        Variable.charactersP1_static[Variable.var_countP1] = str.capitalize(Variable.charactersP1_static[Variable.var_countP1])
        os.system("cls")
        print("WALKA!!!")
        print("=================================")
        print(display(Variable.charactersP1_static, Variable.charactersP2_static))
        print("=================================\n")
        Variable.var_countP1 += 1
    if Variable.var_countP1 == 3:
        print('Player1 killed Player2\n')
        Variable.var_countP1=0
        Variable.killState = True

    try: k = key.char
    except: k = key.name
    if k is Variable.charactersP2_static[Variable.var_countP2] and Variable.killState==False:
        Variable.charactersP2_static[Variable.var_countP2] = str.capitalize(Variable.charactersP2_static[Variable.var_countP2])
        os.system("cls")
        print("WALKA!!!")
        print("=================================")
        print(display(Variable.charactersP1_static, Variable.charactersP2_static))
        print("=================================\n")
        Variable.var_countP2 += 1
    if Variable.var_countP2 == 3:
        print('Player2 killed Player1\n')
        Variable.var_countP2 = 0
        Variable.killState = True


def display(var1, var2):

    lettersString = "Player 1: "

    for i in var1:
        lettersString += i
        lettersString += " "
    lettersString += "\tPlayer 2: "

    for i in var2:
        lettersString += i
        lettersString += " "
    return lettersString

#
# if collision(1,2,1,3):
#     print("WALKA!!!")
#     print("=======================================")
#     print(display(Variable.charactersP1_static, Variable.charactersP2_static))
#     print("=======================================\n")
#
#
# lis = keyboard.Listener(on_press=on_pressPlayer1)
# lis.start()
# lis.join()